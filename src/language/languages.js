const Brand = {
    name: {
        english: "Name",
        chinese: "品牌名称"
    },
    id: {
        english: "ID",
        chinese: "品牌标识"
    },
    status: {
        english: "Status",
        chinese: "品牌状态"
    },
    english: "Brand",
    chinese: "品牌"
};

const Category = {
    name: {
        english: "Name",
        chinese: "分类名称"
    },
    id: {
        english: "ID",
        chinese: "分类标识"
    },
    status: {
        english: "Status",
        chinese: "分类状态"
    },
    parent: {
        english: "Parent",
        chinese: "父分类"
    },
    child: {
        english: "Child",
        chinese: "子分类"
    },
    english: "Category",
    chinese: "分类"
};

const Merchandise = {
    name: {
        english: "Name",
        chinese: "商品名称"
    },
    title: {
        english: "Title",
        chinese: "商品标题"
    },
    description: {
        english: "Detail",
        chinese: "商品细节"
    },
    keyword: {
        english: "Keyword",
        chinese: "商品关键字"
    },
    tag: {
        english: "Tag",
        chinese: "商品标签"
    },
    color: {
        english: "Color",
        chinese: "商品颜色"
    },
    size: {
        english: "Size",
        chinese: "商品尺码"
    },
    stock: {
        english: "Stock",
        chinese: "商品库存"
    },
    rank: {
        english: "Rank",
        chinese: "商品排名"
    },
    id: {
        english: "ID",
        chinese: "商品标识"
    },
    status: {
        english: "Status",
        chinese: "商品状态"
    },
    basic: {
        english: "Basic",
        chinese: "基础信息"
    },
    category: {
        english: "Category",
        chinese: "商品分类"
    },
    color_size: {
        english: "Size&Color",
        chinese: "尺码颜色"
    },
    images: {
        english: "Images",
        chinese: "商品图片"
    },
    material: {
        english: "Material",
        chinese: "商品材质"
    },
    price: {
        english: "Price",
        chinese: "商品价格"
    },
    brand: {
        english: "Brand",
        chinese: "商品品牌"
    },
    manufacturer: {
        english: "Manufacturer",
        chinese: "商品供货商"
    },
    origin: {
        english: "origin",
        chinese: "商品产地"
    },
    english: "Goods",
    chinese: "商品"
};

const Status = {
    normal: {
        english: "normal",
        chinese: "生效中"
    },
    deleted: {
        english: "deleted",
        chinese: "已废弃"
    },
    invalid: {
        english: "invalid",
        chinese: "无效"
    },
    unknown: {
        english: "unknown",
        chinese: "未知"
    },
    english: "Status",
    chinese: "状态"
};

const Color = {
    name: {
        english: "Name",
        chinese: "颜色名称"
    },
    rgba: {
        english: "RgbA",
        chinese: "颜色色值"
    },
    english: "Color",
    chinese: "颜色"
};

const Manufacturer = {
    name: {
        english: "Name",
        chinese: "名称"
    },
    address: {
        english: "Address",
        chinese: "地址"
    },
    email: {
        english: "Email",
        chinese: "邮箱"
    },
    phone: {
        english: "Phone",
        chinese: "手机号码"
    },
    contact: {
        english: "Contact",
        chinese: "联系人"
    },
    english: "Manufacturer",
    chinese: "供货商"
};

const Images = {
    main_front: {
        english: "Front",
        chinese: "正面主图"
    },
    main_back: {
        english: "Back",
        chinese: "背面主图"
    },
    minor: {
        english: "Minor",
        chinese: "附图"
    },
    english: "Image",
    chinese: "图片"
};

const Size = {
    digital_size: {
        english: "Digital size",
        chinese: "数字尺码"
    },
    letter_size: {
        english: "Letter size",
        chinese: "字母尺码"
    },
    english: "Size",
    chinese: "尺码"
};

const Stock = {
    english: "Stock",
    chinese: "库存"
};

const Times = {
    create: {
        english: "createTime",
        chinese: "创建时间"
    },
    update: {
        english: "updateTime",
        chinese: "更新时间"
    },
    delete: {
        english: "deleteTime",
        chinese: "删除时间"
    },
    english: "Time",
    chinese: "时间"
};

const Actions = {
    create: {
        english: "Create",
        chinese: "新增"
    },
    update: {
        english: "Update",
        chinese: "编辑"
    },
    delete: {
        english: "Delete",
        chinese: "废弃"
    },
    export: {
        english: "Export",
        chinese: "导出"
    },
    next: {
        english: "Next",
        chinese: "下一步"
    },
    previous: {
        english: "Prev",
        chinese: "上一步"
    },
    cancel: {
        english: "Cancel",
        chinese: "取消"
    },
    confirm: {
        english: "Confirm",
        chinese: "确认"
    },
    english: "Actions",
    chinese: "操作"
};

export default  {
    Actions,
    Brand,
    Category,
    Color,
    Images,
    Merchandise,
    Manufacturer,
    Size,
    Status,
    Stock,
    Times
}