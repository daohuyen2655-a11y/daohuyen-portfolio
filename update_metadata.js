const fs = require('fs');
const file = 'src/app/layout.tsx';
let code = fs.readFileSync(file, 'utf8');

const oldMetadata = `export const metadata: Metadata = {
  title: "My Scrapbook Portfolio",
  description: "A creative scrapbook style portfolio",
};`;

const newMetadata = `export const metadata: Metadata = {
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
};`;

code = code.replace(oldMetadata, newMetadata);
fs.writeFileSync(file, code);
