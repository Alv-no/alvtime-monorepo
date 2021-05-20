import { mutations, getters, State, state as initialState } from "@/store";

jest.mock("@azure/msal-browser");
jest.mock("../../config.ts");

describe("GET TIMEENTRIES FOR STATISTICS", () => {
  const { getTimeEntriesSummarizedPerMonthPerTask } = getters;
  const thisMonth = new Date();
  const threeMonthsAgo = new Date();
  threeMonthsAgo.setMonth(thisMonth.getMonth() - 3);
  let state: State;
  beforeEach(() => {
    state = {
      ...initialState,
      timeEntries: [
        {
          id: 1,
          date: thisMonth.toISOString().split("T")[0],
          value: "7.5",
          taskId: 17,
        },
        {
          id: 2,
          date: thisMonth.toISOString().split("T")[0],
          value: "7.5",
          taskId: 17,
        },
        {
          id: 3,
          date: thisMonth.toISOString().split("T")[0],
          value: "7.5",
          taskId: 17,
        },
        {
          id: 4,
          date: threeMonthsAgo.toISOString().split("T")[0],
          value: "7.5",
          taskId: 17,
        },
      ],
    };
  });

  it("Get timeentries summarized pr month", () => {
    const res = getTimeEntriesSummarizedPerMonthPerTask(state);
    expect(res[0].summarizedHours[2].value).toEqual(22.5);
  });
});

describe("UPDATE_TIME_ENTRIES", () => {
  const { UPDATE_TIME_ENTRIES } = mutations;
  let state: State;
  beforeEach(() => {
    state = { ...initialState };
  });

  it("Adds timentries to map", () => {
    UPDATE_TIME_ENTRIES(state, [
      { id: 1, date: "2020-02-25", value: "7.5", taskId: 17 },
    ]);

    expect(state.timeEntriesMap).toEqual({
      "2020-02-2517": { value: "7.5", id: 1 },
    });
    expect(state.timeEntries).toEqual([
      { id: 1, date: "2020-02-25", value: "7.5", taskId: 17 },
    ]);
  });

  it("Updates timentries in map", () => {
    UPDATE_TIME_ENTRIES(state, [
      { id: 1, date: "2020-02-25", value: "7.5", taskId: 17 },
    ]);
    UPDATE_TIME_ENTRIES(state, [
      { id: 1, date: "2020-02-25", value: "5", taskId: 17 },
    ]);

    expect(state.timeEntriesMap).toEqual({
      "2020-02-2517": { value: "5", id: 1 },
    });
    expect(state.timeEntries).toEqual([
      { id: 1, date: "2020-02-25", value: "5", taskId: 17 },
    ]);
  });

  it("Add multiple timentries in map on same date", () => {
    UPDATE_TIME_ENTRIES(state, [
      { id: 1, date: "2020-02-25", value: "7.5", taskId: 17 },
      { id: 2, date: "2020-02-25", value: "5", taskId: 13 },
    ]);

    expect(state.timeEntriesMap).toEqual({
      "2020-02-2513": { value: "5", id: 2 },
      "2020-02-2517": { value: "7.5", id: 1 },
    });
    expect(state.timeEntries).toEqual([
      { id: 1, date: "2020-02-25", value: "7.5", taskId: 17 },
      { id: 2, date: "2020-02-25", value: "5", taskId: 13 },
    ]);
  });

  it("Filters timeentries that are only from the last 3 months", () => {});
});
