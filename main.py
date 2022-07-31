from docx import Document
import json
tab = []
document = Document('Никишов .docx')
for table in document.tables:
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                tab.append(para.text)

for para in document.paragraphs:
    tab.append(para.text)

out = []
for i in (1, 3, 5, 7, 9, 18, 20, 23, 24, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 48, 50, 53, -5):
    out.append(tab[i])
    fio = out[0].split()
    out.pop(0)
    for i in range(0, len(fio)):
        out.insert(i, fio[i])
dicts = {}
dicts['fam'] = out[0]
dicts['nam'] = out[1]
dicts['otch'] = out[2]
dicts['bdate'] = out[3]
dicts['wplace'] = out[4]
dicts['staj'] = out[5]
dicts['razr'] = out[6]
dicts['vid'] = out[7]
dicts['method'] = out[8]
dicts['tu'] = out[9]
print(dicts)


zay = {'data':dicts}
with open('data.txt', 'w') as outfile:
    json.dump(zay, outfile)

# var input=document.createElement('input');
#    input.type="file";
#    input.onload = function () {alert(e)}
#
# document.getElementById ('header').appendChild (input);



#
# Ребята! Не знаю, тема актуальна ещё или нет, но я нашел решение! На сайте CodePen был один проект, где загружалась SVG картинка и там парсилась. Спёр код оттуда.
#
# function readFile(object) {
#   var file = object.files[0]
#   var reader = new FileReader()
#   reader.onload = function() {
#     document.getElementById('out').innerHTML = reader.result
#   }
#   reader.readAsText(file)
# }
# <input type="file" id="file">
# <button onclick="readFile(document.getElementById('file'))">Read!</button>
# <div id="out"></div>




# Полная версия скрипта
# console.clear()
# function readFile(object, callback) {
#   var file = object.files[0]
#   console.log(file)
#   var reader = new FileReader()
#   reader.onload = function() {
#   callback(reader.result)
#     console.log(reader)
#   }
#   reader.readAsText(file)
# }
# function saveFile(data, name){
#   var a=document.createElement("a")
#   a.setAttribute("download", name||"file.txt")
#   a.setAttribute("href", "data:application/octet-stream;base64,"+btoa(data||"undefined"))
#   a.click()
# }
# function read(){
#   var file = document.getElementById("file").files[0]
#   console.log("Loading \""+file.name+"\"... ("+Math.round(file.size/1024)+"kB)")
#   if(file.size>=256*1024){
#     if(!confirm("File size is "+Math.round(file.size/1024)+"kBytes! Really want to read it?")){
#       console.log("Aborting loading file...")
#       return
#     }
#   }
#   var reader = new FileReader()
#   reader.onload = function() {
#     console.log("File readed!")
#     const d = reader.result
#     console.log(d)
#     document.getElementById("out").innerHTML=reader.result
#   }
#   console.log("Starting reading file...")
#   reader.readAsText(file)
# }