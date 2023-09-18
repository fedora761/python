repl 에서 실행
- https://replit.com/
 

1. 작업 내용
- https://remoteok.com/
- https://weworkremotely.com/
위 두개 사이트에서 python, java등의 키워드로 검색시 데이터를 취합해 보여줌, 다운로드도 csv로 가능


2. 폴더구조  

nomadcoders
 ┣ file
 ┃ ┣ extractors
 ┃ ┃ ┣ rmw.py
 ┃ ┃ ┗ wwr.py
 ┃ ┣ static
 ┃ ┃ ┣ back_img12.jpg
 ┃ ┃ ┣ back_img13.jpg
 ┃ ┃ ┗ back_img16.png
 ┃ ┣ templates
 ┃ ┃ ┣ home.html
 ┃ ┃ ┗ search.html
 ┃ ┣ file.py
 ┃ ┗ main.py

3. 파일 설명
- main.py 에서 templates 폴더의 home.html, search.html 호춯
- home.html 은 extractors 폴더의 rmw.py, wwr.py 파이선 호출
- 각 html은 static폴더의 img 파일을 사용
- file.py는 검색 결과에 대해 csv 결과로 download 하기 위해 사용
- 
