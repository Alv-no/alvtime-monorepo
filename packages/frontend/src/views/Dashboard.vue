<template>
  <CenterColumnWrapper>
<<<<<<< HEAD
    <h1>Her kan du se oversikt over dine registrerte timer for {{ year }}</h1>
    <div class="chart-container">
      <Chart class="chart" :data="monthSums"></Chart>
=======
    <h1>Halla, dashboard her</h1>
    <div class="chart-container">
      <Chart class="chart" :data="monthSums"></Chart>
      <Chart class="chart"></Chart>
      <Chart class="chart"></Chart>
>>>>>>> 2ce9a6dd5688e1f6489b2cfa22b569b7ef2a49e5
    </div>
  </CenterColumnWrapper>
</template>

<script lang="ts">
import Vue from "vue";
import Chart from "@/components/CommitChart.vue";
import CenterColumnWrapper from "@/components/CenterColumnWrapper.vue";
import moment from "moment";

export default Vue.extend({
  name: "Home",
  components: {
    Chart,
    CenterColumnWrapper,
  },
  beforeCreate() {
    this.$store.dispatch("FETCH_WEEK_ENTRIES");
  },
<<<<<<< HEAD
  data() {
    return {
      year: moment().year(),
    };
  },
=======
>>>>>>> 2ce9a6dd5688e1f6489b2cfa22b569b7ef2a49e5
  computed: {
    monthSums() {
      const timeEntries = this.$store.state.timeEntries;
      if (!timeEntries) return;

      const monthSums: number[] = Array(12).fill(0);
      const thisYear = moment().year();

      for (const timeEntry of timeEntries) {
        const timeEntryYear = moment(timeEntry.date).year();
        const month = moment(timeEntry.date).month();
        const value: number = timeEntry.value;
        if (timeEntryYear === thisYear) {
          monthSums[month] += Number(value);
        }
      }
      return monthSums;
    },
  },
});
</script>

<style scoped>
.chart-container {
  display: flex;
}

.chart {
<<<<<<< HEAD
  width: 50%;
=======
  width: 30%;
>>>>>>> 2ce9a6dd5688e1f6489b2cfa22b569b7ef2a49e5
  margin: 0 10px;
}
</style>
