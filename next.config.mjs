/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ["katex"],
  devIndicators: false,
  compiler: {
    removeConsole:
      process.env.NODE_ENV === "production"
        ? { exclude: ["error", "warn"] }
        : false,
  },
  ...(process.env.NEXT_DIST_DIR ? { distDir: process.env.NEXT_DIST_DIR } : {}),
};

export default nextConfig;
