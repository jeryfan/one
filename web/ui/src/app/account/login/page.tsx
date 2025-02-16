import { GithubSignIn, GoogleSignIn } from "@/components/sign/sign-in";
import Image from "next/image";

const Login = () => {
  return (
    <>
      <div className="bg-[url('/background.png')] bg-cover w-full min-h-screen sm:p-4 lg:p-8 flex justify-center lg:justify-start gap-x-20">
        <div className="flex w-full flex-col bg-white shadow rounded-2xl shrink-0 space-between">
          <div className="flex items-center justify-between p-6 w-full">
            <Image
              src={"/images/taiji.png"}
              alt=""
              width={40}
              height={40}
              className="block"
            />
          </div>
          <div className="flex flex-col items-center w-full grow justify-center px-6 md:px-[108px]">
            <div className="flex flex-col md:w-[400px]">
              <div className="w-full mx-auto mt-8">
                <div className="flex flex-col gap-3 mt-6">
                  <GithubSignIn />
                  <GoogleSignIn />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Login;
