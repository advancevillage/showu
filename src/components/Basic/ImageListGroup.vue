<template>
    <div class="image-list-group" v-bind:style="{width: width + 'px'}">
        <ul>
            <li v-for="(item, index) in items" :key="index">
                <div>
                    <img v-bind:style="{width: height + 'px', height: height + 'px'}" :src="item.imageUrl">
                </div>
                <div class="descriptor" v-bind:style="{width: (1 - height/width) * 100 + '%'}">
                    <span class="operate" @click="del(item, index)"><span class="mdi mdi-close-circle"></span></span>
                    <span v-if="item.value" v-bind:style="{width: '100%', display: 'inline-block'}">{{item.value}}</span>
                    <span v-else v-bind:style="{width: '100%', display: 'inline-block'}">{{item.name[language]}}&nbsp;&nbsp;{{item.color.name[language]}}&nbsp;&nbsp;{{item.size}}</span>
                    <span v-bind:style="{width: '100%', display: 'inline-block'}">{{item.price}}</span>
                    <span v-bind:style="{width: '100%', display: 'inline-block'}"></span>
                    <button v-bind:style="[item.count <= 1 ? {pointerEvents: 'none'}:{}]" @click="decr(item)">-</button>
                    <label>
                        <input v-model="item.count" type="tel" @input="changeCount(item)"/>
                    </label>
                    <button @click="incr(item)">+</button>
                    <span class="price">{{currency + (item.count * item.price).toFixed(1)}}</span>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "ImageListGroup",
        props: {
            items: {
                type: Array,
                required: true,
            },
            width: {
                type: Number,
                required: false,
                default: 280
            },
            height: {
                type: Number,
                required: false,
                default: 64
            },
            language: {
                type: String,
                required: true
            },
            currency: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                languages: this.$languages,
            }
        },
        methods: {
            changeCount(item) {
                item.count = item.count <= 1 ? 1 : item.count;
                item.count = parseInt(item.count)
                this.$emit('update')
            },
            del(item, index) {
                this.items.splice(index, 1);
                this.$emit('del', index)
            },
            incr(item) {
                item.count++;
                this.$emit('incr')
            },
            decr(item) {
                item.count--;
                this.$emit('decr')
            }
        }
    }
</script>

<style scoped>
    .image-list-group {
        height: auto;
    }
    .image-list-group li {
        width: 100%;
        height: 100%;
        float: left;
        border-bottom: 1px solid lightgray;
        border-radius: 6px;
        background: white;
    }
    .image-list-group li:hover {
        background: #f8f8f8;
    }
    .image-list-group li > * {
        display: block;
        float: left;
        position: relative;
    }
    .image-list-group button, .image-list-group input {
        width: 15px;
        height: 15px;
        box-shadow: none;
        outline: none;
        border: none;
        border-radius: 100%;
        background: white;
    }
    .image-list-group input {
        width: 50px;
        text-align: center;
        border-radius: 10px;
    }
    .image-list-group button {
        color: black;
        cursor: pointer;
    }
    .image-list-group button:hover {
        background: black;
        color: white;
    }
    .descriptor {
        padding-left: 5%;
        text-align: left;
    }
    .operate {
        position: absolute;
        margin-right: 3%;
        right: 0;
        cursor: pointer;
        text-decoration: underline;
        font-family: monospace;
        color: black;
    }
    .price {
        float: right;
        margin-right: 3%;
    }
</style>