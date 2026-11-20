/** @type {import('next').NextConfig} */
const nextConfig = {
  distDir: process.env.NEXT_DIST_DIR || ".next",
  devIndicators: false,
  webpack: (config, { dev }) => {
    if (dev) {
      config.cache = {
        type: "memory",
      };
    }
    return config;
  },
};

export default nextConfig;
