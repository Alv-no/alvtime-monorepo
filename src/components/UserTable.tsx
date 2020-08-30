import MaterialTable from "material-table";
import React from "react";
import useSWR from "swr";
import tableIcons from "./tableIcons";
import { fetcher, setCache, globalTableOptions } from "./Tables";

export default function UserTable() {
  const columns = [
    { title: "Navn", field: "name" },
    { title: "E-post", field: "email" },
    { title: "Flexi timer", field: "flexiHours" },
    { title: "Start dato", field: "startDate" },
  ];

  const path = "/api/admin/Users";

  const { data, error } = useSWR(path, fetcher);

  const handleRowAdd = async (newData: any) => {
    setCache(path, [...data, newData]);
    const addedData = await fetcher("/api/admin/CreateUser", {
      method: "post",
      body: [newData],
    });
    setCache(path, [...addedData, ...data]);
  };

  if (error) return <div>Error...</div>;
  return (
    <MaterialTable
      icons={tableIcons}
      title="Users"
      columns={columns}
      data={data}
      isLoading={!data}
      options={{ ...globalTableOptions }}
      editable={{
        onRowAdd: handleRowAdd,
      }}
    />
  );
}