"use client";
import React, { useState } from "react";
import { DownOutlined } from "@ant-design/icons";
import { Button, Dropdown, Space, Checkbox, Menu } from "antd";
import type { MenuProps } from "antd";

const items: MenuProps["items"] = [
  {
    label: (
      <Checkbox onClick={(e) => e.stopPropagation()}>MOR-Hematologia</Checkbox>
    ),
    key: "1",
  },
  {
    label: (
      <Checkbox onClick={(e) => e.stopPropagation()}>MOR - Coagulação</Checkbox>
    ),
    key: "2",
  },
  {
    label: (
      <Checkbox onClick={(e) => e.stopPropagation()}>
        MOR - Química Clínica
      </Checkbox>
    ),
    key: "3",
  },
  {
    label: (
      <Checkbox onClick={(e) => e.stopPropagation()}>
        NTO - Hematologia
      </Checkbox>
    ),
    key: "4",
  },
];

const DropDownFilter: React.FC = () => {
  return (
    <Space wrap>
      <Dropdown menu={{ items }} placement="bottomRight">
        <Button className="dropfilter">
          <Space>
            Setores
            <DownOutlined />
          </Space>
        </Button>
      </Dropdown>
    </Space>
  );
};

export default DropDownFilter;
