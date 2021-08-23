//시ㄴ 
const timeContainer = document.querySelector(".time"),
    // nowHour = timeContainer.querySelector("#hour"),
    // nowMin = timeContainer.querySelector("#minutes"),
    // nowSec = timeContainer.querySelector("#seconds"),
    nowAmpm = timeContainer.querySelector("#period");
    // 아이디 #, 클래스 .

//날ㅏ
const dayContainer = document.querySelector(".date"),
    nowDay = dayContainer.querySelector("#dayname"),
    nowMonth = dayContainer.querySelector("#month"),
    nowDate = dayContainer.querySelector("#daynum"),
    nowYear = dayContainer.querySelector("#year");

//시간 함수 
function getTime(){
    const now = new Date();
    const minutes = now.getMinutes();
    let hours = now.getHours();
    const seconds = now.getSeconds();

    //pm으로 띄기 
    if (hours>=12){
        nowAmpm.innerText="PM"
    }
    if(hours==0){
        hours=12;
    }
    if(hours>12){
        hours = hours - 12;
    }
    //html 에 텍스트넣기 
    // nowHour.innerText = hours<10 ?`0$[hours]`: hours;
    // nowMin.innerText = minutes<10 ? `0$[minutes]` : minutes;
    // nowSec.innerText = seconds<10 ? `0$[seconds]`:seconds;

    let ids = ["hours","minutes","seconds"];
    let values = [hours,minutes,seconds];
    //for문 
    for(let i=0;i<ids.length;i++){
        values[i] = values[i]<10 ? '0'+values[i] : values[i];
        document.getElementById(ids[i]).firstChild.nodeValue = values[i]
    };
  }

//날짜 함수 
function getCalender() {
    const now = new Date();
    const day = now.getDay(); // 요일
    const month = now.getMonth(); // 월
    const date = now.getDate(); // 일
    const year = now.getFullYear(); // 년
  
    //배열형식 
    let week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ];

      //영어 month
    let Emonth = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];

    // nowDay.innerText = day;
    // nowMonth.innerText = month;
    // nowDate.innerText = date;
    // nowYear.innerText = year;
    // nowDay.innerText = week[day];

    let ids = ["dayname","month","daynum","year"];
    let values = [week[day],Emonth[month],date,year];

    //for문 
    for(let i=0;i<ids.length;i++){
        if(i==2)
        {
            values[i] = values[i]<10 ?'0'+values[i]: values[i];
            document.getElementById(ids[i]).firstChild.nodeValue = values[i];    
        }
        document.getElementById(ids[i]).firstChild.nodeValue = values[i];
    }
  }

function init(){
    getTime();
    setInterval(getTime,1000); //초가 흐를수 있게 ! 
    getCalender();
}
init();