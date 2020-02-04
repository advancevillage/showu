<template>
    <div>
        <Header/>
        <div id="container">
            <div class="container_warp">
                <div class="carts">
                    <div class="carts_list">
                        <div class="top">
                        </div>
                        <div class="center">
                            <div class="card" v-for="(item, index) in cart.items" :key="index">
                                <div class="card-content">
                                    <div class="media">
                                        <div class="media-left">
                                            <img class="image" :src="item.imageUrl" alt="Placeholder image">
                                        </div>
                                        <div class="media-content">
                                            <p class="title is-6">{{item.title}}</p>
                                            <p class="subtitle is-7">{{item.size}}</p>
                                            <p class="subtitle is-7">{{item.color}}</p>
                                            <p class="subtitle is-7">{{item.style}}</p>
                                            <b-field class="count_warp">
                                                <b-numberinput v-model="item.sum" readonly="true" class="count" type="is-light" size="is-small"  :min="item.min" :max="item.max" controls-position="compact"></b-numberinput>
                                                <span class="price">{{item.symbol}}{{item.sum * item.price}}</span>
                                            </b-field>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="bottom"></div>
                    </div>
                    <div class="carts_summary">
                        <div style="background: darkgray">
                            <!-- 订单核对头部 -->
                            <nav class="level">
                                <div class="level-item has-text-centered">
                                    <div>
                                        <p class="heading">Order Summary</p>
                                    </div>
                                </div>
                            </nav>
                            <!-- 商品费用 -->
                            <nav class="level">
                                <div class="level-left">
                                    <div class="level-item has-text-centered">
                                        <p class="heading">Subtotal</p>
                                    </div>
                                </div>
                                <div class="level-right">
                                    <div class="level-item has-text-centered">
                                        <p class="heading">Tweets</p>
                                    </div>
                                </div>
                            </nav>
                            <!-- 关税费用 -->
                            <nav class="level">
                                <div class="level-left">
                                    <div class="level-item has-text-centered">
                                        <p class="heading">Tax</p>
                                    </div>
                                </div>
                                <div class="level-right">
                                    <div class="level-item has-text-centered">
                                        <p class="heading">Tweets</p>
                                    </div>
                                </div>
                            </nav>
                            <!-- 配送费用 -->
                            <nav class="level">
                                <div class="level-left">
                                    <div class="level-item has-text-centered">
                                        <p class="heading">Shipping</p>
                                    </div>
                                </div>
                                <div class="level-right">
                                    <div class="level-item has-text-centered">
                                        <p class="heading">Tweets</p>
                                    </div>
                                </div>
                            </nav>
                            <!-- 总费用 -->
                            <nav class="level" v-bind:style="{'padding-bottom': '1.5rem'}">
                                <div class="level-left">
                                    <div class="level-item has-text-centered">
                                        <p class="heading">Total</p>
                                    </div>
                                </div>
                                <div class="level-right">
                                    <div class="level-item has-text-centered">
                                        <p class="heading">Tweets</p>
                                    </div>
                                </div>
                            </nav>
                        </div>
                        <!-- 继续 -->
                        <nav class="level" v-bind:style="{'padding-left': 0, 'padding-right': 0}">
                            <b-button type="is-dark" expanded>CONTINUE TO CHECKOUT</b-button>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header from '../common/Header'
    import Footer from '../common/Footer'

    export default {
        name: "Cart",
        components: {
            Header,
            Footer
        },
        data() {
            return {
                cart: {
                    items: [
                        {
                            title: "The Teddy Crew Neck Sweater",
                            size:  "Size: L",
                            color: "Color: Red",
                            style: "Style: Boo",
                            sum: 2,
                            min: 1,
                            max: 10,
                            price: 99,
                            symbol: "$",
                            imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_150,q_auto/v1/i/dc11f623_3d5f.jpg"},
                        {
                            title: "The Teddy Crew Neck Sweater",
                            size:  "Size: L",
                            color: "Color: Red",
                            style: "Style: Boo",
                            sum: 2,
                            min: 1,
                            max: 10,
                            price: 99,
                            symbol: "$",
                            imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_150,q_auto/v1/i/dc11f623_3d5f.jpg"},
                        {
                            title: "The Teddy Crew Neck Sweater",
                            size:  "Size: L",
                            color: "Color: Red",
                            style: "Style: Boo",
                            sum: 2,
                            min: 1,
                            max: 10,
                            price: 99,
                            symbol: "$",
                            imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_150,q_auto/v1/i/dc11f623_3d5f.jpg"},
                        {
                            title: "The Teddy Crew Neck Sweater",
                            size:  "Size: L",
                            color: "Color: Red",
                            style: "Style: Boo",
                            sum: 2,
                            min: 1,
                            max: 10,
                            price: 99,
                            symbol: "$",
                            imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_150,q_auto/v1/i/dc11f623_3d5f.jpg"},
                        {
                            title: "The Teddy Crew Neck Sweater",
                            size:  "Size: L",
                            color: "Color: Red",
                            style: "Style: Boo",
                            sum: 2,
                            min: 1,
                            max: 10,
                            price: 99,
                            symbol: "$",
                            imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_150,q_auto/v1/i/dc11f623_3d5f.jpg"},
                        {
                            title: "The Teddy Crew Neck Sweater",
                            size:  "Size: L",
                            color: "Color: Red",
                            style: "Style: Boo",
                            sum: 2,
                            min: 1,
                            max: 10,
                            price: 99,
                            symbol: "$",
                            imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_150,q_auto/v1/i/dc11f623_3d5f.jpg"}
                    ]
                }
            }
        }
    }
</script>

<style scoped>
    .container_warp {
        width: 100%;
        min-height: 740px;
        margin-top: 60px;
        float: left;
    }
    .carts {
        width: 100%;
        height: 100%;
        padding: 0 15%;
    }
    .carts > .carts_list, .carts > .carts_summary {
        float: left;
        height: 100%;
    }
    .carts > .carts_list {
        width: 60%;
    }
    .carts > .carts_summary {
        width: 30%;
        margin-left: 5%;
    }
    .carts > .carts_list > .top, .carts > .carts_list > .center, .carts > .carts_list > .bottom {
        width: 100%;
    }
    .card-content {
        padding: 0;
    }
    .image {
        width: 150px;
        height: 150px;
    }
    .subtitle {
        margin: 0;
        padding: 0;
    }
    .count_warp {
        margin-top: 10px;
        float: left;
        width: 100%;
    }
    .count {
        width: 80%;
    }
    .level {
        border-top: 1px solid gray;
        padding-top: 1.5rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
    .carts > .carts_list > .center > .card {
        margin-bottom: 2%;
    }
</style>


