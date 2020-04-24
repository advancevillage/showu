<template>
    <div>
        <!-- 用户详情页 -->
        <div class="user_base">
            <nav class="level">
                <div class="level-item has-text-centered">
                </div>
                <div class="level-item has-text-centered">
                </div>
                <div class="level-item has-text-centered">
                </div>
            </nav>
            <div class="list_item" v-for="i in 3" :key=i>
                <ul v-if="i === 1">
                    <li><span class="column">{{languages.Account.email[language]}}</span></li>
                    <li><span class="column">{{languages.Account.password[language]}}</span>
                        <span></span>
                        <span><b-icon icon="square-edit-outline" style="cursor: pointer"></b-icon></span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="user_shipping_address">
            <nav class="level">
                <div class="level-item has-text-centered">
                </div>
                <div class="level-item has-text-centered">
                    <span>{{languages.Account.shippingAddress[language]}}</span>
                </div>
                <div class="level-item has-text-centered">
                </div>
            </nav>
            <div class="list_item" v-for="(item, index) in address.items" :key=index style="min-height: 200px; border: 1px solid lightgray;">
                <ul>
                    <!-- 物流信息 -->
                    <li style="position: relative;"><span>
                        <label><input v-model="address.selected" type="radio" checked :value=index style="height: 25px"></label>
                        <label><b-icon icon="square-edit-outline" style="cursor: pointer"></b-icon></label>
                    </span></li>
                    <li><span class="column"></span><span>{{ item.fullName}}</span></li>
                    <li v-if="item.line1.length > 0"><span class="column"></span><span>{{ item.line1}}</span></li>
                    <li v-if="item.line2.length > 0"><span class="column"></span><span>{{ item.line2}}</span></li>
                    <li><span class="column"></span><span>{{ item.city}}&nbsp;&nbsp;{{ item.province}}&nbsp;&nbsp;{{ item.country}}</span></li>
                    <li><span class="column"></span><span>{{ item.phone}}</span></li>
                    <li><span class="column"></span><span>{{ item.zipCode}}</span></li>
                </ul>
            </div>
        </div>
        <div class="user_billing_address">
            <nav class="level">
                <div class="level-item has-text-centered">
                </div>
                <div class="level-item has-text-centered">
                    <span>{{languages.Account.billingAddress[language]}}</span>
                </div>
                <div class="level-item has-text-centered">
                </div>
            </nav>
            <div class="list_item" v-for="(item, index) in address.items" :key=index style="min-height: 200px; border: 1px solid lightgray;">
                <ul>
                    <!-- 物流信息 -->
                    <li style="position: relative;"><span>
                        <label><input v-model="address.selected" type="radio" checked :value=index style="height: 25px"></label>
                        <label><b-icon icon="square-edit-outline" style="cursor: pointer"></b-icon></label>
                    </span></li>
                    <li><span class="column"></span><span>{{ item.fullName}}</span></li>
                    <li v-if="item.line1.length > 0"><span class="column"></span><span>{{ item.line1}}</span></li>
                    <li v-if="item.line2.length > 0"><span class="column"></span><span>{{ item.line2}}</span></li>
                    <li><span class="column"></span><span>{{ item.city}}&nbsp;&nbsp;{{ item.province}}&nbsp;&nbsp;{{ item.country}}</span></li>
                    <li><span class="column"></span><span>{{ item.phone}}</span></li>
                    <li><span class="column"></span><span>{{ item.zipCode}}</span></li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "User",
        mounted() {
            this.QueryAddress();
        },
        data() {
            return {
                language: "chinese",
                languages: this.$languages,
                address: {
                    items: [],
                    total: 0,
                    selected: -1
                }
            }
        },
        methods: {
            async QueryAddress() {
                const header = {
                    "x-language": this.language,
                };
                const params = {};
                let data = await this.$api.QueryAddress(header, params) || {};
                if (data.hasOwnProperty("code")) {
                    console.log(data);
                } else {
                    this.address.total = data.total;
                    this.address.items = data.items;
                    for (let i = 0; i < this.address.items.length; i++) {
                        if (this.address.items[i].isDefault) {
                            this.address.selected = i;
                            break;
                        } else {
                            this.address.selected = -1;
                        }
                    }
                }
            },
            back() {
                this.$router.push({path: '/account?href=order'})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(-1);
                    });
            },
        }
    }
</script>

<style scoped>
    .user_base, .user_shipping_address, .user_billing_address {
        width: 100%;
        height: auto;
        float: left;
        margin-bottom: 2%;
        padding-top: 2%;
        padding-bottom: 2%;
        display: block;
        font-family: serif;
        font-size: smaller;
    }
    .list_item{
        width: 31%;
        height: 100%;
        float: left;
        margin: 0 1% 1%;
    }
    .list_item ul{
        display: block;
        border: none;
    }
    .list_item ul li {
        height: 25px;
    }
    .column, .list_item ul li span {
        text-align: right;
        display: inline-block;
        width: 30%;
    }
    .level-item {
        border: 1px solid;
    }
</style>