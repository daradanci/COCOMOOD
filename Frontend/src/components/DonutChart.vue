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
            // text: 'in tonnes',
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
              { label: 'Планируется', y: 1, color: '#0039A6' },
              { label: 'Прочитано', y: 4, color: '#DE2910' },
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
