from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree
import urllib.parse as urlparse, os

# List of video file extension and format supported
# key is the file extension (in lowercase), value the mime type
VIDEO_FORMATS = {
    '.mp4': "video/mp4",
    '.mpeg4': "video/mp4",
    '.mpg4': "video/mp4",
    '.webm': "video/webm",
    '.ogg': "video/ogg",
    '.ogv': "video/ogg",
    '.ogm': "video/ogg",
}

class InlineVideoProcessor(Treeprocessor):
    def run(self, root):
        for element in root.iter('img'):
            attrib = element.attrib
            if 'src' in attrib and attrib['src'] != "":
                # extract the extension of the image
                path = urlparse.urlparse(attrib['src']).path
                _, ext = os.path.splitext(path)
                if ext == "":
                    continue
                ext = ext.lower()
                if ext not in VIDEO_FORMATS:
                    continue

                tail = element.tail
                element.clear()
                element.tag = 'video'
                element.tail = tail

                element.text = "Your browser does not handle the video "
                video_link = etree.SubElement(element, "a")
                video_link.set("href", attrib['src'])
                video_link.text = attrib['src']

                element.set('controls', "controls")
                source = etree.SubElement(element, "source")
                source.set('src', attrib['src'])
                source.set('type', VIDEO_FORMATS[ext])

                del attrib['src']
                for k, v in attrib.items():
                    element.set(k, v)


class VideoExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(InlineVideoProcessor(md), 'inlinevideoprocessor', 15)


def makeExtension(**kwargs):
    return VideoExtension(**kwargs)
