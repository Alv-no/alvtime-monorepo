<template>
  <div class="padding">
    <md-table>
      <md-table-row>
        <md-table-head>Task</md-table-head>
        <md-table-head
          v-for="month in getRelevantMonths"
          :key="month.getMonth()"
        >
          {{ month.toLocaleString("no-nb", { month: "long" }) }}
        </md-table-head>
      </md-table-row>
      <md-table-row v-for="row in getTimeEntriesSummed" :key="row.id">
        <md-table-cell>{{
          row[0] ? row[0].project.name + " - " + row[0].name : "Missing name"
        }}</md-table-cell>
        <md-table-cell
          v-for="element in row.slice(1, 4)"
          :key="element.date.getMonth()"
        >
          {{ element.value }}
        </md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import config from "@/config";
import { FrontendTimentrie } from "@/store/timeEntries";
import tasks, { Task } from "../store/tasks";
import moment, { Moment, months } from "moment";

interface TimeEntriesDateFormated {
  [key: string]: string | number | Date | Object;
  id: number;
  value: number;
  date: Date;
  taskId: number;
}

interface TimeEntriesPerTask {
  [key: number]: TimeEntriesDateFormated;
}

interface TimePerTaskSum {
  id: number;
  value: number;
}

export default Vue.extend({
  name: "Summarizedhours",

  computed: {
    getTimeEntriesSummed() {
      return this.$store.getters.getTimeEntriesSummarizedPerMonthPerTask;
    },

    getRelevantMonths() {
      return this.$store.getters.getRelevantMonthsForStatiscts;
    },
  },

  beforeCreate() {
    this.$store.commit("CREATE_WEEKS");
    this.$store.dispatch("FETCH_WEEK_ENTRIES");
  },
});
</script>

<style scoped>
.padding {
  padding: 1rem;
}
</style>
