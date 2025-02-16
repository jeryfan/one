import { signIn } from "@/auth";
import { FaGithub } from "react-icons/fa";
import { FcGoogle } from "react-icons/fc";
import { Button } from "@/components/ui/button";

export function GithubSignIn() {
  return (
    <form
      action={async () => {
        "use server";
        await signIn("github");
      }}
    >
      <Button
        variant="outline"
        type="submit"
        className="w-full flex items-center justify-center space-x-2 rounded-lg border-gray-300"
      >
        <FaGithub />
        <span>使用 GitHub 登录</span>
      </Button>
    </form>
  );
}

export function GoogleSignIn() {
  return (
    <form
      action={async () => {
        "use server";
        await signIn("github");
      }}
    >
      <Button
        type="submit"
        variant="outline"
        className="w-full flex items-center justify-center space-x-2 rounded-lg border-gray-300"
      >
        <FcGoogle />
        <span>使用 Google 登录</span>
      </Button>
    </form>
  );
}
