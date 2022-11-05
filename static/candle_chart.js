// Read Excel
/*
function read_excel(filename){

    var reader = new FileReader();
    var filename = reader.result;
    
    var wb = XLSX.read(filename, {type : 'binary'});

    wb.SheetNames.forEach(function(sheetName){
        var rowObj = XLSX.utils.sheet_to_json(wb.Sheets[sheetName]);
        console.log(JSON.stringify(rowObj));
    })
    reader.readAsBinaryString(input.files[0]);
    
}*/

function draw_chart(x_data, y_data){
    var context = document.getElementById('myChart').getContext('2d');

    var myChart = new Chart(context, {
    type: 'line', // 차트의 형태
    data: { // 차트에 들어갈 데이터
        labels: x_data,
            //x 축
        datasets: [
            { //데이터
                //label: '토출온도', //차트 제목
                fill: true, // line 형태일 때, 선 안쪽을 채우는지 안채우는지
                data: y_data,//x축 label에 대응되는 데이터 값
                
                backgroundColor: [
                    //색상
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],

                borderColor: [
                    //경계선 색상
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1 //경계선 굵기
            }
        ]
    },
    options: {
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true
                    }
                }
            ]
        }
    }
    });
}