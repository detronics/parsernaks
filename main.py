from docx import Document
import json
import os, glob
import re
filename = glob.glob('Input\*.docx')

dicts = {}
tab = []
vids = {}
document = Document(filename[0])
for table in document.tables:
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                tab.append(para.text)
parag1 = []
for para in document.paragraphs:
    parag1.append(para.text)


def searchinncity(parag):
    for i in parag:
        if re.fullmatch('\d{10}', i):
            dicts['inn'] = i
    city = re.findall('\sг.[а-яА-ЯёЁ\s]+', parag[4])
    dicts['city'] = city[0]



def searchvid(sp):
    mets = []
    for i in range(0,len(sp)):
        if sp[i] == 'производственных объектов (ТУ ОПО)':
            i += 1
            while sp[i] != '2.4. Шифр НД по сварке':
                if len(sp[i]) > 1:
                    mets.append(sp[i])
                i += 1
    formatvid(sp=mets)


def formatvid(sp):
    for i in sp:
        osn = re.findall('[А-Я]+', i)[0]
        dop =','.join(re.findall('п[.\s]\d+', i))
        vids[osn] = dop


out = []
for i in (1, 3, 5, 7, 9, 18, 20, 23, 24, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 48, 50, 53, -5, ):
    out.append(tab[i])
    fio = out[0].split()
    out.pop(0)
    for i in range(0, len(fio)):
        out.insert(i, fio[i])

searchvid(sp=tab)
dicts['fam'] = out[0]
dicts['nam'] = out[1]
dicts['otch'] = out[2]
dicts['bdate'] = out[3]
dicts['wplace'] = out[4][:-6]+'Газпром Трансгаз Нижний Новгород'
dicts['staj'] = out[5]
dicts['razr'] = out[6]
dicts['vid'] = out[7]
dicts['method'] = re.findall('[А-Я]+', out[8])[0]
dicts['group']=vids
searchinncity(parag=parag1)
print(dicts)
with open('Out/data.txt', 'w') as outfile:
    json.dump(dicts, outfile)

# for file in glob.glob("Input\*"):
#     os.remove(file)




#  рабочая версия
# // ==UserScript==
# // @name         Script1
# // @namespace    http://tampermonkey.net/
# // @version      0.1
# // @description  try to take over the world!
# // @author       You
# // @match        https://ac.naks.ru/ac_personal/
# // @icon         https://www.google.com/s2/favicons?sz=64&domain=naks.ru
# // @grant        GM_registerMenuCommand
# // @run-at       context-menu
# // ==/UserScript==
#
# window.addEventListener("DOMContentLoaded", event => {
#     var dd=document.createElement('input');
#     dd.type="file";
#     dd.id = '4';
#     document.getElementById ('navigation').appendChild (dd);
#    var input1=document.createElement('input');
#    input1.type="button";
#    input1.value = 'Записать1';
#    input1.onclick = readFile;
#    document.getElementById ('navigation').appendChild (input1);
#    var input2=document.createElement('input');
#    input2.type="button";
#    input2.value = 'Записать2';
#    input2.onclick = readFile2;
#    document.getElementById ('navigation').appendChild (input2);
# });
#
# function readFile() {
#   var obj = document.getElementById('4');
#   var file = obj.files[0];
#   var reader = new FileReader();
#   reader.onload = function() {
#      var fam = document.getElementsByName('prop[last_name]')[0];
#      var nam = document.getElementsByName('prop[name]')[0];
#      var otch = document.getElementsByName('prop[second_name]')[0];
#      var wplace = document.getElementsByName('prop[company]')[0];
#      var inn = document.getElementsByName('prop[company_inn]')[0];
#      var city = document.getElementsByName('prop[city]')[0];
#      var zay = document.getElementsByName('fiz')[0];
#      var vid = document.getElementsByName('prop[vid_att]')[0];
#      var spos = document.getElementsByName('prop[svarka]')[0];
#      var prof = document.getElementsByName('prop[position]')[0];
#      prof.value = "Сварщик";
#      zay.value = 1;
#      const loaddata = reader.result;
#      var mydata = JSON.parse(loaddata);
#      fam.value = mydata.fam;
#      nam.value = mydata.nam;
#      otch.value = mydata.otch;
#      wplace.value = mydata.wplace;
#       inn.value = mydata.inn;
#       city.value = mydata.city;
#       if (mydata.vid == 'Дополнительная'){
#           vid.value = 96198;}
#       else if (mydata.vid == 'Периодическая'){
#           vid.value = 96195;}
#       else {};
#       if (mydata.method =='РД'){
#           spos.value = 36;}
#       else if (mydata.method == 'Г'){
#           spos.value = 51;}
#       else if (mydata.method == 'РАД'){
#           spos.value = 34;}
#       else if (mydata.method == 'Т'){
#           spos.value = 2094;}
#       else if (mydata.method == 'МП'){
#           spos.value = 65;}
#       else if (mydata.method == 'МПС'){
#           spos.value = 58;}
#       else if (mydata.method == 'НИ'){
#           spos.value = 40;}
#       else if (mydata.method == 'ЗН'){
#           spos.value = 39;}
#       else if (mydata.method == 'АПГ'){
#           spos.value = 63;}
#       else {};
#
#   }
#   reader.readAsText(file)
# }
#
# function readFile2(){
#     var obj = document.getElementById('4');
#     var file = obj.files[0];
#     var reader = new FileReader();
#     reader.onload = function() {
#         const loaddata = reader.result;
#         var mydata = JSON.parse(loaddata);
#         var vklad = document.getElementsByName('prop[dop_att]')[0];
#         var vid = document.getElementsByName('prop[vid_att]')[0];
#         if ( vid.value == 96198){
#             vklad.value = "В1"};
#         var inputs = document.getElementsByTagName('input');
#         var pao = document.getElementsByName('gazprom1')[0];
#         var jj = window.mydata;
#         var keys_v = Object.keys(mydata.group);
#         for (let i in keys_v){
#             if( keys_v[i] == 'ГО'){
#                 inputs[61].checked=true;
#                 if (mydata.group['ГО'].indexOf('п.1') !== -1){
#                     inputs[62].checked=true;}
#                 if (mydata.group['ГО'].indexOf('п.2') !== -1){
#                     inputs[63].checked=true;}
#                 if (mydata.group['ГО'].indexOf('п.2п') !== -1){
#                     inputs[64].checked=true;}
#                 if (mydata.group['ГО'].indexOf('п.3') !== -1){
#                     inputs[65].checked=true;}
#                 if (mydata.group['ГО'].indexOf('п.4') !== -1){
#                     inputs[66].checked=true;}
#                 }
#             else if (keys_v[i] == 'КО'){
#                 inputs[71].checked=true;
#                 if (mydata.group['КО'].indexOf('п.1') !== -1){
#                     inputs[72].checked=true;}
#                 if (mydata.group['КО'].indexOf('п.2') !== -1){
#                     inputs[73].checked=true;}
#                 if (mydata.group['КО'].indexOf('п.3') !== -1){
#                     inputs[74].checked=true;}
#                 if (mydata.group['КО'].indexOf('п.4') !== -1){
#                     inputs[75].checked=true;}
#             }
#             else if (keys_v[i] == 'СК'){
#                 inputs[140].checked=true;
#                 if (mydata.group['СК'].indexOf('п.1') !== -1){
#                     inputs[141].checked=true;}
#                 if (mydata.group['СК'].indexOf('п.2') !== -1){
#                     inputs[142].checked=true;}
#                 if (mydata.group['СК'].indexOf('п.3') !== -1){
#                     inputs[143].checked=true;}
#                 if (mydata.group['СК'].indexOf('п.4') !== -1){
#                     inputs[144].checked=true;}
#             }
#             else if (keys_v[i] == 'НГДО'){
#                 inputs[86].checked=true;
#                 pao.checked=true;
#                 if (mydata.group['НГДО'].indexOf('п.3') !== -1){
#                     inputs[89].checked=true;}
#                 if (mydata.group['НГДО'].indexOf('п.4') !== -1){
#                     inputs[90].checked=true;}
#                 if (mydata.group['НГДО'].indexOf('п.10') !== -1){
#                     inputs[96].checked=true;}
#                 if (mydata.group['НГДО'].indexOf('п.13') !== -1){
#                     inputs[99].checked=true;}
#             }}
# }
#     reader.readAsText(file);
# }