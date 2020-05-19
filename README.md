# JobScraper
***
## 요약
* nomadcoder의 'python으로 web Scraper 만들기' 강의를 보며 만든 scraper입니다. (2020.05.19 작동 - 이후 사이트 변경에 따라 동작 안 할 수 있음)
* Stackoverflow와 indeed에서 특정 keyword를 넣으면 Job title, location, company name, apply link 등이 요약되어 검색됩니다. (현재는 Stackoverflow의 job scraper만 scraper.py에 포함되어있습니다.  indeed는 indeed.py로 scraping할 수 있지만 main.py에서 동작하려면 수정이 조금 필요합니다.)
* Flask를 통해 웹사이트를 만든 후 웹에서 확인하거나 csv 형태로 다운받을 수 있게 하였습니다. 
* 실제 DB가 아닌 fake DB를 메모리에 저장하여 키워드를 재검색할 때 시간이 걸리지 않고 바로 확인할 수 있습니다(물론 실시간 데이터는 아닙니다.. ) 또한 서버를 재시작하면 reset됩니다. 

## 소회
scraper를 만든게 처음은 아니지만 많은 경력을 가지고 있는 개발자가 scraper를 어떤 식으로 만드는지 직접 볼 수 있어서 도움이 많이 됐습니다. 문제를 정의하고 필요한 부분들을 나눠서 만들고 합치는 과정들이 인상적이었습니다. 짧은 시간이지만 Flask로 웹사이트를 만들어보는 것도 재밌는 경험이었습니다. 다음에느 Django를 이용해보고 둘을 비교해보는 시간을 가져볼까 합니다. 
