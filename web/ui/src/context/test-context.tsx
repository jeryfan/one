"use client";

import { useState, type FC } from "react";
import { createContext, useContext } from "use-context-selector";

export type TestContextValue = {
  name: string;
  setName: (name: string) => void;
};

export const TestContext = createContext<TestContextValue>({
  name: "",
  setName: () => {},
});

export type TestContextProviderProps = {
  children: React.ReactNode;
};

export const TestContextProvider: FC<TestContextProviderProps> = ({
  children,
}) => {
  const [name, setName] = useState<string>("");
  return (
    <TestContext.Provider value={{ name, setName }}>
      {children}
    </TestContext.Provider>
  );
};

export const useTestContext = () => useContext(TestContext);
