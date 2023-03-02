# 圖片物件偵測網站

### 2023/03/02

◆ 實作使用者驗證功能
- 使用者註冊功能
- 編輯使用者功能
- 刪除使用者功能
- 登入功能
- 登出功能

◆ 程式目錄架構
```
.
├── apps
│   ├── app.py
│   ├── auth
│   │   ├── forms.py
│   │   ├── templates
│   │   │   └── auth
│   │   │       ├── base.html
│   │   │       ├── index.html
│   │   │       ├── login.html
│   │   │       └── signup.html
│   │   └── views.py
│   ├── config.py
│   └── crud
│       ├── forms.py
│       ├── models.py
│       ├── static
│       │   └── style.css
│       ├── templates
│       │   └── crud
│       │       ├── base.html
│       │       ├── create.html
│       │       ├── edit.html
│       │       └── index.html
│       └── views.py
├── .env
├── .gitignore
├── local.sqlite
└── tree.txt
```
