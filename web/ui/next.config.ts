import type { NextConfig } from "next"

const nextConfig: NextConfig = {
    /* config options here */
    output: "export",
    basePath: "/one",
    assetPrefix: "/one",
    images: {
        unoptimized: true,
    },
}

export default nextConfig
