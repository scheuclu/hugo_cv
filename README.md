## YAML CV

This REPO contains my CV.

I derive both my [wepage-CV](scheuclu.com/hugo_cv) as well as my PDF-CV from a common [YAML file](./data).
This reduces my workload a lot, and also makes it much easier to make changes.

Here's what the rendered CV looks like:


<img src="https://awesomescreenshot.s3.amazonaws.com/image/3871678/34137765-8b72a7d1c8d91c7ad7a00f4edd5429c7.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20221107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221107T122915Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=eb1be90f2e560b4ab183afa72a7e6b6ab3a90a4d98bda85e28403a9f6e1bc2db" width="50%" >

## How to make changes
1. Edit the yaml file under [data](./data).
2. The webpage is automatically published on submit top Github.
3. The latex file need to be generated manually for now via [pdfgen/convert.py](pdfgen/convert.py). I want to automate this on submit in the future.

## Generated PDFs
https://www.overleaf.com/docs?snip_uri=https://raw.githubusercontent.com/scheuclu/hugo_cv/main/pdfgen/content.tex
