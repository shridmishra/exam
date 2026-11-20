/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ["katex"],
  devIndicators: false,
  ...(process.env.NEXT_DIST_DIR ? { distDir: process.env.NEXT_DIST_DIR } : {}),
};

export default nextConfig;
