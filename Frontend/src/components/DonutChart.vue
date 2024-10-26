<template>
  <CanvasJSChart :options="options" :styles="styleOptions" />
</template>

<script>
export default {
  data() {
    return {
      options: {
        theme: 'light2',
        animationEnabled: true,
        title: {
          text: 'Соотношение планируемого и прочитанного',
        },
        subtitles: [
          {
            text: 'in tonnes',
          },
        ],
        data: [
          {
            type: 'doughnut',
            startAngle: 90,
            indexLabel: '{label} {y}(#percent%)',
            yValueFormatString: '#,##0K',
            toolTipContent:
              "<span style='\"'color: {color};'\"'>{label}</span>, {y} tonnes",
            dataPoints: [
              { label: 'Планируется', y: 4500, color: '#DE2910' },
              { label: 'Прочитано', y: 600, color: '#0039A6' },
              // { label: 'India', y: 370, color: '#F79432' },
              // { label: 'United States Of America', y: 320, color: '#37366B' },
              // { label: 'Brazil', y: 210, color: '#F5D900' },
              // { label: 'Malaysia', y: 150, color: '#F7C600' },
              // { label: 'Others', y: 876, color: '#7a7677' },
            ],
          },
        ],
      },
      styleOptions: {
        width: '100%',
        height: '360px',
      },
    }
  },
}
</script>
