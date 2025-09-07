# content-models
Model(s) for automated content generation with development and upload pipelines

## Pipeline (NEWS MODEL)
1) Stream or periodically check news stories related to finance
> Consider IQFEED  
> Yahoo Finance  
> Other source (scraping?)  
2) Request data for given ticker affected via yahoo finance rest api
3) Summarize the given story and data into ~240 word script (OpenAI API) including context, impact, etc.
4) Source images, screenshots, charts, relating to story (OpenAI and Scraping)
5) Generate caption, hashtags, thumbnail, title, category, for final video
6) YouTube Devloper v3 API for upload 