<template>
  <div>
    <h2 class="ratetitle">오늘의 환율</h2>
    <div class="table-container">
      <table class="table" style="white-space: nowrap; width:850px;">
        <thead>
          <tr>
            <th style="width: 20%">번호</th>
            <th style="width: 20%">국가</th>
            <th style="width: 30%">화폐</th>
            <th style="width: 30%">환율(1 화폐단위 당 '원')</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, idx) in ratelist" :key="item.id">
            <td>{{ idx + 1 }}</td>
            <td>{{ item.country }}</td>
            <td>{{ item.currency }}</td>
            <td>{{ item.rate }}</td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>
</template>

<script>
export default {
  name: 'RateList',
  props:{
    ratelist: Array
  },
  data() {
    return {
    }
  },

  methods: {

  }
}

</script>

<style>
.table-container {
  display: flex;
  justify-content: center;
  text-align: center;
}

.ratetitle {
  text-align: center;
}

</style>