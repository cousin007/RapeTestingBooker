# 撩鼻預約機

## User Guide
1. Download Python>=3.7 (64-bit)
2. Add python to your environment variable
3. Install library with cmd: 
```
pip install selenium
pip install json
```
4. Download source code: `Code > Download ZIP`
5. Edit config.json (Explanation below)
6. Run Main.py
7. Pray and wait

## Configuration
Edit config.json to fill in your information.
|key|Description|
|-|-|
|id|ID card no without checksum. eg.A123456|
|checksum| ID card checksum. eg.7|
|zh_surname|中文姓 eg.陳|
|zh_name|中文名 eg.大文|
|tel|phone no. eg. 95645425|
|districts| Prefered testing center location. Please enter center code in list format.<br /> Center code: <br />1 : 離島區<br /> 2 : 葵青區<br /> 3 : 北區<br /> 4 : 西貢區<br /> 5 : 沙田區<br /> 6 : 大埔區<br /> 7 : 荃灣區<br /> 8 : 屯門區<br /> 9 : 元朗區<br /> 10 : 九龍城區<br /> 11 : 觀塘區<br /> 12 : 深水埗區<br /> 13 : 黃大仙區<br /> 14 : 油尖旺區<br /> 15 : 中西區<br /> 16 : 東區<br /> 17 : 南區<br /> 18 : 灣仔區<br />例子︰如果我想揀觀塘、黃大仙、沙田，應該點寫?<br />Ans: [11,13,5]<br />**請必須揀2個或以上地區**|
|date|想Book幾多日內既日期 range:0-15 (0為當天)<br />例如，我想book3日內既日子:<br />[0,1,2]|

Completed config.json should look like:
```json
{
    "id": "a123456",
    "checksum": "7",
    "zh_surname": "陳",
    "zh_name": "大文",
    "tel": "95645425",
    "districts": [11,13,5],
    "date": [0,1,2]
}
```
## Update Notes
### Beta 1.0 - 17/2/2022


