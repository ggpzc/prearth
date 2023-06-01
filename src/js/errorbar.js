
var chartDom = document.getElementById('errorbar');
var myChart = echarts.init(chartDom);
var option;


var categoryData = [];
var errorData = [];
var barData = [];
var dataCount = 20;
var lineCount = 3;
colors = ["#D89C7A", "#849B91", "#8A95A9"]
for (var i = 0; i < dataCount; i++) {
  categoryData.push('category' + i);
}
for (var j = 0; j < lineCount; j++) {
    errorData.push([]);
    barData.push([]);
    for (var i = 0; i < dataCount; i++) {
      var val = Math.random() * 1000;
      
      errorData[j].push([
        i,
        echarts.number.round(Math.max(0, val - Math.random() * 100)),
        echarts.number.round(val + Math.random() * 80)
      ]);
      barData[j].push(echarts.number.round(val, 2));
  }
}



option = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
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
    data: ['bar', 'error']
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
    data: categoryData,
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




for (var i = 0; i < lineCount; i++)
{
  option.legend.data.push("line"+i, "error"+i)
  option.series.push({
      type: 'line',
      name: 'line'+i,
      smooth: true,
      data: barData[i],
      itemStyle: {
        color: colors[i]
      }
    });
  option.series.push({
      type: 'custom',
      name: 'error'+i,
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
        y: [1, 2]
      },
      data: errorData[i],
      z: 100
    })
}



option && myChart.setOption(option);
