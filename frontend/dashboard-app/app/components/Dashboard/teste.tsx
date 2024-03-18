import React from "react";
import { Table } from "antd";
import type { TableColumnsType, TableProps } from "antd";

interface DataType {
  key: React.Key;
  name: string;
  age: number;
  address: string;
}

const columns: TableColumnsType<DataType> = [
  {
    title: "Name",
    dataIndex: "name",
    filters: [
      {
        text: "Joe",
        value: "Joe",
      },
      {
        text: "Jim",
        value: "Jim",
      },
    ],
    // specify the condition of filtering result
    // here is that finding the name started with `value`
    onFilter: (value: string | boolean | React.Key, record) => {
      if (typeof value === "string") {
        return record.name.indexOf(value) === 0;
      }
      return false; // ou outra lógica, se aplicável, para outros tipos de filtro
    },
    sortDirections: ["descend"],
  },
  {
    title: "Age",
    dataIndex: "age",
    defaultSortOrder: "descend",
    sorter: (a, b) => a.age - b.age,
  },
  {
    title: "Address",
    dataIndex: "address",
    filters: [
      {
        text: "London",
        value: "London",
      },
      {
        text: "New York",
        value: "New York",
      },
    ],
    onFilter: (value: string | boolean | React.Key, record) => {
      if (typeof value === "string") {
        return record.name.indexOf(value) === 0;
      }
      return false; // ou outra lógica, se aplicável, para outros tipos de filtro
    },
  },
];

const data = [
  {
    key: "1",
    name: "John Brown",
    age: 32,
    address: "New York No. 1 Lake Park",
  },
  {
    key: "2",
    name: "Jim Green",
    age: 42,
    address: "London No. 1 Lake Park",
  },
  {
    key: "3",
    name: "Joe Black",
    age: 32,
    address: "Sydney No. 1 Lake Park",
  },
  {
    key: "4",
    name: "Jim Red",
    age: 32,
    address: "London No. 2 Lake Park",
  },
];

const onChange: TableProps<DataType>["onChange"] = (
  pagination,
  filters,
  sorter,
  extra
) => {
  console.log("params", pagination, filters, sorter, extra);
};

const App: React.FC = () => (
  <Table columns={columns} dataSource={data} onChange={onChange} />
);

export default App;
