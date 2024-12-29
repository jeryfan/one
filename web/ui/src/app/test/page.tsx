"use client";

import { useTestContext } from "@/context/test-context";

const TestPage = () => {
  const { name, setName } = useTestContext();
  console.log(name);

  return (
    <div>
      <h1>Test Page</h1>
      <p>Name: {name}</p>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
      />
    </div>
  );
};

export default TestPage;
