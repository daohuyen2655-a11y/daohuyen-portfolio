import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Creative Portfolio | Đào Huyền",
  description: "Chào mừng bạn đến với Creative Portfolio của Đào Huyền - Nơi lưu giữ những mẩu chuyện và hành trình sáng tạo đầy màu sắc.",
  openGraph: {
    title: "Creative Portfolio | Đào Huyền",
    description: "Khám phá hành trình sáng tạo và những dự án thiết kế mang đậm dấu ấn cá nhân của Đào Huyền.",
    url: "https://daohuyen-portfolio.vercel.app",
    siteName: "Đào Huyền Portfolio",
    images: [
      {
        url: "/assets/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Đào Huyền - Creative Portfolio",
      },
    ],
    locale: "vi_VN",
    type: "website",
  },
  icons: {
    icon: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        {/* Using Balsamiq Sans for the bouncy scrapbook feel, and Quicksand for body text */}
        <link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400;1,700&family=Fredoka:wght@300..700&family=Quicksand:wght@300..700&display=swap" rel="stylesheet" />
      </head>
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
