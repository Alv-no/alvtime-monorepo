<script lang="ts">
import { Bar } from "vue-chartjs";
import Vue from "vue";

export default Vue.extend({
  props: {
    data: {
      type: Object as () => number[],
    },
  },
  extends: Bar,
  mounted() {
    // Overwriting base render method with actual data.
    this.renderChart({
      labels: [
<<<<<<< HEAD
        "Januar",
        "Februar",
        "Mars",
        "April",
        "Mai",
        "Juni",
        "Juli",
        "August",
        "September",
        "Oktober",
        "November",
        "Desember",
      ],
      datasets: [
        {
          label: "Timer registrert",
=======
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
      ],
      datasets: [
        {
          label: "Hours recorded",
>>>>>>> 2ce9a6dd5688e1f6489b2cfa22b569b7ef2a49e5
          backgroundColor: "#f87979",
          data: this.data,
        },
      ],
    });
  },
});
</script>
