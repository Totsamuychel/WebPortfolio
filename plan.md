проверить код и как работает сайт перед отправкой на гитхаб
1. Загрузить изменения на GitHub: "https://github.com/Totsamuychel/WebPortfolio"
   1     git add .
   2     git commit -m "Add static site generation for GH Pages"
   3     git push origin main
   2. Настроить GitHub Pages:
       * Зайди в свой репозиторий на GitHub.
       * Перейди в Settings -> Pages.
       * В разделе Build and deployment выбери Source: Deploy from a branch.
       * В поле Branch выбери main, а в папке выбери /docs.
       * Нажми Save.