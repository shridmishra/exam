import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
  	container: {
  		center: true,
  		padding: {
  			DEFAULT: '1rem',
  			sm: '1.5rem',
  			lg: '2rem',
  		},
  		screens: {
  			'2xl': '1280px'
  		}
  	},
  	extend: {
  		fontFamily: {
  			sans: ['var(--font-sans)', 'Inter', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'sans-serif'],
  			mono: ['var(--font-mono)', 'var(--font-sans)', 'Inter', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'sans-serif'],
  			'aeonik-medium': ['var(--font-sans)', 'Inter', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'sans-serif'],
  		},
  		fontSize: {
  			h1: [
  				'56px',
  				{
  					lineHeight: '72px',
  					fontWeight: '700'
  				}
  			],
  			h2: [
  				'40px',
  				{
  					lineHeight: '56px',
  					fontWeight: '700'
  				}
  			],
  			h3: [
  				'28px',
  				{
  					lineHeight: '40px',
  					fontWeight: '500'
  				}
  			],
  			h4: [
  				'26px',
  				{
  					lineHeight: '32px',
  					fontWeight: '400'
  				}
  			],
  			h5: [
  				'22px',
  				{
  					lineHeight: '32px',
  					fontWeight: '400'
  				}
  			],
  			h6: [
  				'20px',
  				{
  					lineHeight: '28px',
  					fontWeight: '400'
  				}
  			],
  			'body-lg': [
  				'16px',
  				{
  					lineHeight: '27px',
  					fontWeight: '500'
  				}
  			],
  			'body-md': [
  				'14.5px',
  				{
  					lineHeight: '22px',
  					fontWeight: '500'
  				}
  			],
  			'body-sm': [
  				'13px',
  				{
  					lineHeight: '18px',
  					fontWeight: '400'
  				}
  			],
  			button: [
  				'14px',
  				{
  					lineHeight: '21px',
  					fontWeight: '600'
  				}
  			],
  			stat: [
  				'24px',
  				{
  					lineHeight: '32px',
  					fontWeight: '500'
  				}
  			]
  		},
  		colors: {
  			border: 'hsl(var(--border))',
  			input: 'hsl(var(--input))',
  			ring: 'hsl(var(--ring))',
  			background: 'hsl(var(--background))',
  			foreground: 'hsl(var(--foreground))',
  			primary: {
  				DEFAULT: 'hsl(var(--primary))',
  				foreground: 'hsl(var(--primary-foreground))'
  			},
  			secondary: {
  				DEFAULT: 'hsl(var(--secondary))',
  				foreground: 'hsl(var(--secondary-foreground))'
  			},
  			destructive: {
  				DEFAULT: 'hsl(var(--destructive))',
  				foreground: 'hsl(var(--destructive-foreground))'
  			},
  			success: {
  				DEFAULT: 'hsl(var(--success))',
  				foreground: 'hsl(var(--success-foreground))'
  			},
  			muted: {
  				DEFAULT: 'hsl(var(--muted))',
  				foreground: 'hsl(var(--muted-foreground))'
  			},
  			accent: {
  				DEFAULT: 'hsl(var(--accent))',
  				foreground: 'hsl(var(--accent-foreground))'
  			},
  			popover: {
  				DEFAULT: 'hsl(var(--popover))',
  				foreground: 'hsl(var(--popover-foreground))'
  			},
  			card: {
  				DEFAULT: 'hsl(var(--card))',
  				foreground: 'hsl(var(--card-foreground))'
  			},
  			'filter-active': {
  				DEFAULT: 'hsl(var(--filter-active-bg))',
  				foreground: 'hsl(var(--filter-active-fg))'
  			},
  			year: {
  				'2022': {
  					bg: 'var(--badge-year-2022-bg)',
  					fg: 'var(--badge-year-2022-fg)'
  				},
  				'2023': {
  					bg: 'var(--badge-year-2023-bg)',
  					fg: 'var(--badge-year-2023-fg)'
  				},
  				'2024': {
  					bg: 'var(--badge-year-2024-bg)',
  					fg: 'var(--badge-year-2024-fg)'
  				},
  				'2025': {
  					bg: 'var(--badge-year-2025-bg)',
  					fg: 'var(--badge-year-2025-fg)'
  				}
  			}
  		},
  		borderRadius: {
  			lg: 'var(--radius)',
  			md: 'calc(var(--radius) - 2px)',
  			sm: 'calc(var(--radius) - 4px)'
  		},
  		keyframes: {
  			'accordion-down': {
  				from: {
  					height: '0'
  				},
  				to: {
  					height: 'var(--radix-accordion-content-height)'
  				}
  			},
  			'accordion-up': {
  				from: {
  					height: 'var(--radix-accordion-content-height)'
  				},
  				to: {
  					height: '0'
  				}
  			}
  		},
  		animation: {
  			'accordion-down': 'accordion-down 0.2s ease-out',
  			'accordion-up': 'accordion-up 0.2s ease-out'
  		}
  	}
  },
  plugins: [],
};

export default config;
