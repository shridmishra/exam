/** @type {import('next').NextConfig} */
const isDev = process.env.NODE_ENV === "development";

const nextConfig = {
  // Use separate build directories for development (.next-dev) and production (.next)
  // so that running 'npm run build' or tests never corrupts a running 'npm run dev' server!
  distDir: process.env.NEXT_DIST_DIR || (isDev ? ".next-dev" : ".next"),
  serverExternalPackages: ["katex"],
  devIndicators: false,
  compiler: {
    removeConsole:
      process.env.NODE_ENV === "production"
        ? { exclude: ["error", "warn"] }
        : false,
  },
};

export default nextConfig;
