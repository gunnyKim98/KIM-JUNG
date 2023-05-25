<template>
  <div>
    <h5>상품명 : {{selectedProduct.상품정보['fin_prdt_nm']}}</h5>
    <p>상품 정보가 없는 가입 기간은 데이터가 출력되지 않습니다.</p>
    <canvas
      ref="barChart"
    />
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)

export default {
  props:{
    selectedProduct: Object
  },
  data:() => ({
    type: 'bar',
    data: {
      labels: [ '6개월', '12개월', '24개월', '36개월' ],
      datasets: [{
        label: '저축금리',
        data: [ 0, 0, 0, 0],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
        ],
        borderWidth: 1
      },
      {
        label: '최대우대금리',
        data: [ 0,0,0,0 ],
        backgroundColor: [

          'rgba(54, 162, 235, 0.2)',
          
        ],
        borderColor: [

          'rgba(54, 162, 235, 1)',
          
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          min: 2.0,
          max: 5.0
        }
      }
    }
  }),
  mounted(){
    this.createChart()
  },
  methods:{
    createChart(){
      if (this.selectedProduct['6개월'] !='상품정보없음'){
        this.data.datasets[0].data[0] = this.selectedProduct['6개월']['intr_rate']
      }
      if (this.selectedProduct['12개월'] !='상품정보없음'){
        this.data.datasets[0].data[1] = this.selectedProduct['12개월']['intr_rate']
      }
      if (this.selectedProduct['24개월'] !='상품정보없음'){
        this.data.datasets[0].data[2] = this.selectedProduct['24개월']['intr_rate']
      }
      if (this.selectedProduct['36개월'] !='상품정보없음'){
        this.data.datasets[0].data[3] = this.selectedProduct['36개월']['intr_rate']
      }

      if (this.selectedProduct['6개월'] !='상품정보없음'){
        this.data.datasets[1].data[0] = this.selectedProduct['6개월']['intr_rate2']
      }
      if (this.selectedProduct['12개월'] !='상품정보없음'){
        this.data.datasets[1].data[1] = this.selectedProduct['12개월']['intr_rate2']
      }
      if (this.selectedProduct['24개월'] !='상품정보없음'){
        this.data.datasets[1].data[2] = this.selectedProduct['24개월']['intr_rate2']
      }
      if (this.selectedProduct['36개월'] !='상품정보없음'){
        this.data.datasets[1].data[3] = this.selectedProduct['36개월']['intr_rate2']
      }

      new Chart(this.$refs.barChart, {
        type:'bar',
        data:this.data,
        options:this.options
      })

    }
  }
}
</script>