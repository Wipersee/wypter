// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';


window.onload = function(){
  fetch('http://127.0.0.1:8000/api/pie_chart/'+user_pk+'/')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    chart_datas = [];
    chart_labels=[];
    dict = {};
   for(var i = 0; i < data.length; i++){
    buf = data[i]['category']['name'];
      if (dict[buf]){
        dict[buf] = dict[buf] + parseFloat(data[i]['price']);
      }
      else{
        dict[buf] = parseFloat(data[i]['price']);
      }
   }
   k = Object.keys(dict);
   v = Object.values(dict);
   for(var i = 0; i < k.length; i++){
    chart_datas.push(v[i]);
    chart_labels.push(k[i]);
   }

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: chart_labels,
    datasets: [{
      data: chart_datas,
      backgroundColor: ['#fcba03', '#fc3903', '#00ff62', '#00aeff', '#fc6f03', '#7f00b5','#7bfc03'],
      
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 2,
      xPadding: 15,
      yPadding: 15,
      displayColors: true,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 65,
  },
});

})}