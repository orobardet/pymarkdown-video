# pymarkdown-video

Extension for [python-markdown](https://python-markdown.github.io/), that will convert markdown picture that are vide
file into the HTML5 `video` tag instead of the `img` tag.

## Example

```markdown
![Big Buck Bunny](http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4 "Big Buck Bunny video")
```

will be rendered as

```html
<p>
    <video alt="Big Buck Bunny" controls="controls" title="Vidéo de Big Buck Bunny">
        Your browser does not handle the video <a href="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4">http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4</a>
        <source src="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" type="video/mp4"></source>
    </video>
</p>
```

## Usage

```shell
pip install pymarkdown-video
```

```python
from markdown import Markdown

text = '![Big Buck Bunny](http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4 "Big Buck Bunny video")'
md = Markdown(extensions=['pymarkdown-video'])
print(md.convert(text))
```

You can also use it with [MkDocs](https://www.mkdocs.org/).  
After installing the package with pip, in your `mkdocs.yml`, add:

```yaml
markdown_extensions:
  - pymarkdown-video
```