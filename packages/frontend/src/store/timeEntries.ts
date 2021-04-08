import { State } from "./index";
import { ActionContext } from "vuex";
import { debounce } from "lodash";
import config from "@/config";
import { adAuthenticatedFetch } from "@/services/auth";
import { Task } from "./tasks";

export interface TimeEntrieState {
  timeEntries: FrontendTimentrie[] | null;
  timeEntriesMap: TimeEntrieMap;
  pushQueue: FrontendTimentrie[];
}

export interface FrontendTimentrie {
  id: number;
  date: string;
  value: string;
  taskId: number;
}

export interface TimeEntrieMap {
  [key: string]: TimeEntrieObj;
}

export interface TimeEntrieObj {
  value: string;
  id: number;
}

export interface ServerSideTimeEntrie {
  id: number;
  date: string;
  value: number;
  taskId: number;
}

export interface TimeEntriesDateFormated {
  [key: string]: string | number | Date | Object;
  id: number;
  value: number;
  date: Date;
  taskId: number;
}

const state = {
  timeEntries: null,
  pushQueue: [],
  timeEntriesMap: {},
};

const getters = {
  getTimeEntriesSummarizedPerMonthPerTask: (state: State) => {
    return monthSumPrTask(state.timeEntries, state.tasks);
  },

  getRelevantMonthsForStatiscts: (state: State) => {
    return getRelevantMonths();
  },
};

const mutations = {
  UPDATE_TIME_ENTRIES(state: State, paramEntries: FrontendTimentrie[]) {
    updateTimeEntries(state, paramEntries);
  },
  UPDATE_TIME_ENTRIES_AFTER_UPDATE(
    state: State,
    paramEntries: FrontendTimentrie[]
  ) {
    updateTimeEntries(state, paramEntries);
  },
  ADD_TO_PUSH_QUEUE(state: State, paramEntrie: FrontendTimentrie) {
    state.pushQueue = updateArrayWith(state.pushQueue, paramEntrie);
  },

  FLUSH_PUSH_QUEUE(state: State) {
    state.pushQueue = [];
  },
};

const actions = {
  UPDATE_TIME_ENTRIE(
    { commit, dispatch }: ActionContext<State, State>,
    paramEntrie: FrontendTimentrie
  ) {
    commit("UPDATE_TIME_ENTRIES", [paramEntrie]);
    commit("ADD_TO_PUSH_QUEUE", paramEntrie);
    dispatch("DEBOUNCED_PUSH_TIME_ENTRIES");
  },

  DEBOUNCED_PUSH_TIME_ENTRIES: debounce(
    async ({ state, commit }: ActionContext<State, State>) => {
      const timeEntriesToPush = ([...state.pushQueue]
        .filter(entrie => isFloat(entrie.value))
        .map(createServerSideTimeEntrie)
        .filter(shouldBeStoredServerSide) as unknown) as ServerSideTimeEntrie[];

      if (!timeEntriesToPush.length) return;

      commit("FLUSH_PUSH_QUEUE");
      try {
        const response = await adAuthenticatedFetch(
          config.API_HOST + "/api/user/TimeEntries",
          {
            method: "post",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(timeEntriesToPush),
          }
        );
        const timeEntries = await response.json();
        if (response.status !== 200) {
          throw Error(`${response.statusText}
${timeEntries.title}`);
        }
        if (!Array.isArray(timeEntries) && timeEntries.message) {
          throw Error(timeEntries.message);
        }
        if (Array.isArray(timeEntries)) {
          commit(
            "UPDATE_TIME_ENTRIES_AFTER_UPDATE",
            timeEntries.map(createTimeEntrie)
          );
        }
      } catch (e) {
        console.error(e);
        commit("ADD_TO_ERROR_LIST", e);
      }
    },
    1000
  ),

  FETCH_TIME_ENTRIES: async (
    { commit }: ActionContext<State, State>,
    params: { fromDateInclusive: string; toDateInclusive: string }
  ) => {
    const url = new URL(config.API_HOST + "/api/user/TimeEntries");
    url.search = new URLSearchParams(params).toString();

    try {
      const res = await adAuthenticatedFetch(url.toString());
      const timeEntries = await res.json();
      if (!Array.isArray(timeEntries) && timeEntries.message) {
        throw Error(timeEntries.message);
      }
      const frontendTimeEntries = timeEntries
        .filter((entrie: ServerSideTimeEntrie) => entrie.value)
        .map(createTimeEntrie);
      commit("UPDATE_TIME_ENTRIES", frontendTimeEntries);
    } catch (e) {
      console.error(e);
      commit("ADD_TO_ERROR_LIST", e);
    }
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};

function updateTimeEntrieMap(
  timeEntrieMap: TimeEntrieMap,
  paramEntrie: FrontendTimentrie
): TimeEntrieMap {
  timeEntrieMap[`${paramEntrie.date}${paramEntrie.taskId}`] = {
    value: paramEntrie.value,
    id: paramEntrie.id,
  };
  return timeEntrieMap;
}

function updateArrayWith(
  arr: FrontendTimentrie[],
  paramEntrie: FrontendTimentrie
) {
  const index = arr.findIndex(entrie => isMatchingEntrie(paramEntrie, entrie));

  if (index !== -1) {
    return [
      ...arr.map(entrie =>
        isMatchingEntrie(paramEntrie, entrie) ? paramEntrie : entrie
      ),
    ];
  } else {
    return [...arr, paramEntrie];
  }
}

function isMatchingEntrie(
  entrieA: FrontendTimentrie,
  entrieB: FrontendTimentrie
) {
  return entrieA.date === entrieB.date && entrieA.taskId === entrieB.taskId;
}

function createTimeEntrie(data: any): FrontendTimentrie {
  return {
    ...data,
    date: data.date.split("T")[0],
    value: data.value.toString(),
  };
}

function createServerSideTimeEntrie(timeEntrie: FrontendTimentrie) {
  return {
    ...timeEntrie,
    value: Number(timeEntrie.value.replace(",", ".")),
  };
}

export function isFloat(str: string) {
  const commaMatches = str.match(/[.,]/g);
  const isMoreThanOneComma = commaMatches && commaMatches.length > 1;
  const isOnlyDigitsAndComma = !str.match(/[^0-9.,]/g);
  return isOnlyDigitsAndComma && !isMoreThanOneComma;
}

function shouldBeStoredServerSide(paramEntrie: ServerSideTimeEntrie) {
  return !isNonEntrieSetToZero(paramEntrie);
}

function isNonEntrieSetToZero(paramEntrie: ServerSideTimeEntrie) {
  return paramEntrie.value === 0 && paramEntrie.id === 0;
}

function updateTimeEntries(state: State, paramEntries: FrontendTimentrie[]) {
  let newTimeEntriesMap = { ...state.timeEntriesMap };
  for (const paramEntrie of paramEntries) {
    newTimeEntriesMap = updateTimeEntrieMap(newTimeEntriesMap, paramEntrie);
  }
  state.timeEntriesMap = { ...state.timeEntriesMap, ...newTimeEntriesMap };
<<<<<<< HEAD

  let newTimeEntries = state.timeEntries ? [...state.timeEntries] : [];
  for (const paramEntrie of paramEntries) {
    newTimeEntries = updateArrayWith(newTimeEntries, paramEntrie);
  }
  state.timeEntries = newTimeEntries;
}

function getRelevantMonths(): Date[] {
  const today = new Date();
  const lastMonth = new Date(today.getFullYear(), today.getMonth() - 1);
  const twoMonthsAgo = new Date(
    lastMonth.getFullYear(),
    lastMonth.getMonth() - 1
  );
  const relevantMonths = [twoMonthsAgo, lastMonth, today];
  return relevantMonths;
}

function filterTimeEntriesByRelevantMonths(
  allTimeEntriesAllTasks: TimeEntriesDateFormated[][]
) {
  return allTimeEntriesAllTasks.map(timeEntriesSingleTask => {
    return timeEntriesSingleTask.filter(x => {
      return getRelevantMonths().some(y => {
        if (y.getMonth() == x.date.getMonth()) {
          return y;
        }
      });
    });
  });
}

function convertStringToDateAndValueToNumber(
  timeEntries: FrontendTimentrie[] | null
) {
  var newArray: TimeEntriesDateFormated[] = timeEntries
    ? timeEntries.map((x: FrontendTimentrie) => {
        let newObj = {
          id: x.id,
          value: Number(x.value),
          taskId: x.taskId,
          date: new Date(x.date),
        };
        return newObj;
      })
    : [];
  return newArray;
}

function splitIntoTasks(
  timeEntriesFormated: TimeEntriesDateFormated[]
): TimeEntriesDateFormated[][] {
  var uniqueTasks = [...new Set(timeEntriesFormated.map(x => x.taskId))];

  var hoursPrTask = uniqueTasks.map(x => {
    return timeEntriesFormated.filter(y => y.taskId === x);
  });

  return hoursPrTask;
}

function monthSum(x: any): any {
  let initArray = getRelevantMonths().map(x => {
    return {
      date: x,
      value: 0,
    };
  });
  var value = x.reduce((acc: any, cur: any) => {
    let existItem = acc.find(
      (x: TimeEntriesDateFormated) => cur.date.getMonth() == x.date.getMonth()
    );
    if (existItem) {
      existItem.value += cur.value;
    } else {
      acc.push(cur);
    }
    return acc;
  }, initArray);
  return value;
}

function monthSumPrTask(
  allTimeEntries: FrontendTimentrie[] | null,
  allTasks: Task[]
) {
  const timeEntriesFormated = convertStringToDateAndValueToNumber(
    allTimeEntries
  );
  const timeEntriesSplitIntoTasks = splitIntoTasks(timeEntriesFormated);
  const onlyRelevantTimeEntries = filterTimeEntriesByRelevantMonths(
    timeEntriesSplitIntoTasks
  );
  var values = onlyRelevantTimeEntries.map(x => {
    if (Object.keys(x).length !== 0) {
      var taskForArray = allTasks.filter((task: Task) => {
        if (task !== undefined && task.id === x[0].taskId) {
          return [task];
        }
      });
      return taskForArray.concat(monthSum(x));
    }
  });
  var finalValues = values.filter((x: any) => {
    return x;
  });
  return finalValues;
=======

  let newTimeEntries = state.timeEntries ? [...state.timeEntries] : [];
  for (const paramEntrie of paramEntries) {
    newTimeEntries = updateArrayWith(newTimeEntries, paramEntrie);
  }
  state.timeEntries = newTimeEntries;
>>>>>>> master
}
