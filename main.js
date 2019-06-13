// date
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1;
var yyyy = today.getFullYear();
var date = today.getDay();
// var date_dict = {
//     0: 'Sunday',
//     1: 'Monday',
//     2: 'Tuesday',
//     3: 'Wednesday',
//     4: 'Thursday',
//     5: 'Friday',
//     6: 'Saturday'
// }
var date_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

console.log(mm+'/'+dd+'/'+yyyy+', '+date_list[date]);
document.getElementById("date").innerHTML = mm+'/'+dd+'/'+yyyy+', '+date_list[date];

// tabs
function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

// select-all checkbox
var checkboxes = document.querySelectorAll('input.meat-sub'),
    checkall = document.getElementById('meat');

for(var i=0; i<checkboxes.length; i++) {
  checkboxes[i].onclick = function() {
    var checkedCount = document.querySelectorAll('input.meat-sub:checked').length;

    checkall.checked = checkedCount > 0;
    checkall.indeterminate = checkedCount > 0 && checkedCount < checkboxes.length;
  }
}

checkall.onclick = function() {
  for(var i=0; i<checkboxes.length; i++) {
    checkboxes[i].checked = this.checked;
  }
}