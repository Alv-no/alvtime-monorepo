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
      <md-table-row v-for="row in monthSumPrTask" :key="row.id">
        <md-table-cell>{{
          row[0] ? row[0].project.name + " - " + row[0].name : "hei"
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

const MONTHS = [
  "Januar",
  "Februar",
  "Mars",
  "April",
  "Mars",
  "Juni",
  "Juli",
  "August",
  "September",
  "Oktober",
  "November",
  "Desember",
];

export default Vue.extend({
  name: "Summarizedhours",

  computed: {
    monthSumPrTask(): any {
      var onlyRelevantTimeEntries = this.filterTimeEntriesByRelevantMonths(
        this.splitIntoTasks
      );
      var values = onlyRelevantTimeEntries.map((x) => {
        if (Object.keys(x).length !== 0) {
          var taskForArray = this.tasks.filter((task: Task) => {
            if (task !== undefined && task.id === x[0].taskId) {
              return [task];
            }
          });
          return taskForArray.concat(this.monthSum(x));
        }
      });
      var finalValues = values.filter((x: any) => {
        return x;
      });
      return finalValues;
    },

    getRelevantMonths(): Date[] {
      const today = new Date();
      const lastMonth = new Date(today.getFullYear(), today.getMonth() - 1);
      const twoMonthsAgo = new Date(
        lastMonth.getFullYear(),
        lastMonth.getMonth() - 1
      );
      const relevantMonths = [twoMonthsAgo, lastMonth, today];
      return relevantMonths;
    },

    splitIntoTasks(): TimeEntriesDateFormated[][] {
      // TODO: FIKSE TYPER HER
      var allTimeEntries = this.convertStringToDate;
      var uniqueTasks = [...new Set(allTimeEntries.map((x) => x.taskId))];

      var hoursPrTask = uniqueTasks.map((x) => {
        return allTimeEntries.filter((y) => y.taskId === x);
      });

      return hoursPrTask;
    },

    convertStringToDate() {
      var newArray: TimeEntriesDateFormated[] = this.getAllTimeEntries.map(
        (x: FrontendTimentrie) => {
          let newObj = {
            id: x.id,
            value: Number(x.value),
            taskId: x.taskId,
            date: new Date(x.date),
          };
          return newObj;
        }
      );
      return newArray;
    },

    getAllTimeEntries() {
      const timeEntries: FrontendTimentrie[] = this.$store.state.timeEntries
        ? this.$store.state.timeEntries
        : [];
      return timeEntries;
    },

    tasks(): any {
      return this.$store.state.tasks;
    },
  },

  beforeCreate() {
    this.$store.commit("CREATE_WEEKS");
    this.$store.dispatch("FETCH_WEEK_ENTRIES");
  },

  methods: {
    filterTimeEntriesByRelevantMonths(
      allTimeEntriesAllTasks: TimeEntriesDateFormated[][]
    ) {
      return allTimeEntriesAllTasks.map((timeEntriesSingleTask) => {
        return timeEntriesSingleTask.filter((x) => {
          return this.getRelevantMonths.some((y) => {
            if (y.getMonth() == x.date.getMonth()) {
              return y;
            }
          });
        });
      });
    },

    monthSum(x: any): any {
      let initArray = this.getRelevantMonths.map((x) => {
        return {
          date: x,
          value: 0,
        };
      });
      var value = x.reduce((acc: any, cur: any) => {
        let existItem = acc.find(
          (x: TimeEntriesDateFormated) =>
            cur.date.getMonth() == x.date.getMonth()
        );
        if (existItem) {
          existItem.value += cur.value;
        } else {
          acc.push(cur);
        }
        return acc;
      }, initArray);
      return value;
    },
  },
});
</script>

<style scoped>
.padding {
  padding: 1rem;
}
</style>
