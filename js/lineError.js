
var chartDom = document.getElementById('lineError');
var myChart = echarts.init(chartDom);
var option;



var colors = ["#D89C7A", "#849B91", "#8A95A9"]
// read data from local position'../data/sex_female.json'



option = {
  tooltip: {
    // trigger: 'axis',
  },
  title: {
    text: '',
    subtext: 'Fake Data',
    left: 'center',
    textStyle: {
       fontWeight: 'bolder'
       
    }
    
  },
  legend: {
    orient: 'vertical',
    left: 'right',
    data: []
  },
  dataZoom: [
    {
      type: 'slider',
      start: 50,
      end: 70
    },
    {
      type: 'inside',
      start: 50,
      end: 70
    }
  ],
  xAxis: {
    // data: years,
    axisLabel : {
      fontSize : '18',
    },

  },
  yAxis: {
    axisLabel : {
      fontSize : '18',
    },
  },
  series: [
  ],
};

// import raw_data from '../data/sex_male.json';




function updateGraph(datapath) {
  fetch(datapath)
  .then(response => response.json())
  .then(json => {
    // empty option.series
    option.series = [];

    var errorData = [];
    var lineData = [];
    var dataCount;
    var lineCount;

    var raw_data = json;
    console.log(raw_data)
    years = raw_data.years;
    keys = raw_data.keys;
    data = raw_data.data;
    option.xAxis.data = years;
    dataCount = keys.length;
    lineCount = years.length;
    for(var i = 0; i < dataCount; i++)
    {
      option.legend.data.push(keys[i]);
      option.legend.data.push("error-"+keys[i]);
      lineData.push([]);
      errorData.push([]);
      for(var j = 0; j < lineCount; j++)
      {
        lineData[i].push(data[i][j][0]);
        errorData[i].push([j, data[i][j][1], data[i][j][2], data[i][j][0]]);
      }
    }
    console.log(lineData);
    console.log(errorData);
    for (var i = 0; i < dataCount; i++)
    {
      option.series.push({
          type: 'line',
          name: keys[i],
          smooth: true,
          data: lineData[i],
          itemStyle: {
            color: colors[i]
          }
        });
      option.series.push({
          type: 'custom',
          name: 'error-'+keys[i],
          itemStyle: {
            borderWidth: 1.5,
            color: colors[i],
          },
          renderItem: function (params, api) {
            var xValue = api.value(0);
            var highPoint = api.coord([xValue, api.value(1)]);
            var lowPoint = api.coord([xValue, api.value(2)]);
            var halfWidth = api.size([1, 0])[0] * 0.1;
            var style = api.style({
              stroke: api.visual('color'),
              fill: undefined
            });
            return {
              type: 'group',
              children: [
                {
                  type: 'line',
                  transition: ['shape'],
                  shape: {
                    x1: highPoint[0] - halfWidth,
                    y1: highPoint[1],
                    x2: highPoint[0] + halfWidth,
                    y2: highPoint[1]
                  },
                  style: style
                },
                {
                  type: 'line',
                  transition: ['shape'],
                  shape: {
                    x1: highPoint[0],
                    y1: highPoint[1],
                    x2: lowPoint[0],
                    y2: lowPoint[1]
                  },
                  style: style
                },
                {
                  type: 'line',
                  transition: ['shape'],
                  shape: {
                    x1: lowPoint[0] - halfWidth,
                    y1: lowPoint[1],
                    x2: lowPoint[0] + halfWidth,
                    y2: lowPoint[1]
                  },
                  style: style
                }
              ]
            };
          },
          encode: {
            x: 0,
            y: [1, 2],
            tooltip: [3,1,2],
          },
          dimensions: ["year", "low","high","avg"],
          data: errorData[i],
          z: 100
        })
    }
    console.log("ok")
    option && myChart.setOption(option);
  });
}

updateGraph("../data/sex.json")
// sleep for 5 seconds

setTimeout(() => {
  updateGraph("../data/age.json")
}, "3000");

  
  
  

// for (var i = 0; i < dataCount; i++) {
//   categoryData.push('category' + i);
// }
// for (var j = 0; j < lineCount; j++) {
//     errorData.push([]);
//     barData.push([]);
//     for (var i = 0; i < dataCount; i++) {
//       var val = Math.random() * 1000;
      
//       errorData[j].push([
//         i,
//         echarts.number.round(Math.max(0, val - Math.random() * 100)),
//         echarts.number.round(val + Math.random() * 80)
//       ]);
//       barData[j].push(echarts.number.round(val, 2));
//   }
// }








