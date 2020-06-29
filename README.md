# ME30-Website (Tufts, Fall 2020)

### Working on the Website
This site is built using Hugo. Hugo can be installed for your OS [here](https://gohugo.io/getting-started/installing/)  
It must then be built by running `hugo` in the top level directory. This will generate a `public/` folder.  
Inside the `public/` folder, you may run an HTTP server to view the content locally (this is easiest by doing `python3 -m http.server`)  

### Adding new Pages
All main content for this site is stored in the `content/` folder, and then organized by topic. All site pages are rendered automatically from markdown files (`.md` extension), and creating new ones will automatically integrate them into the website according to where they are located in the file structure. For a markdown cheat-sheet, check [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
