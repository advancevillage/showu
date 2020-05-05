<template>
    <div class="tag-group" v-bind:style="{width: width + 'px', height: (25 * items.length/3 + height) + 'px'}">
        <header>
            <p v-if="title.length > 0" v-bind:style="{width: (100 - 6 - 1 - (clear.length * 7) * 100 / width) + '%'}">{{title}}</p>
            <button v-if="clear.length > 0" v-bind:style="{width: ((clear.length * 7) * 100 / width) + '%'}" @click="reset">{{clear}}</button>
        </header>
        <section>
            <span v-for="(item, index) in items" :key="index" v-bind:style="[item.selected ? {background: 'black', fontWeight: 'bolder', color: 'white'} : {}]" v-on:click="get(index)">
                {{item.value}}
            </span>
        </section>
    </div>
</template>

<script>
    export default {
        name: "TagGroup",
        props: {
            items: {
                type: Array,
                required: true,
            },
            width: {
                type: Number,
                required: false,
                default: 200
            },
            height: {
                type: Number,
                required: false,
                default: 100
            },
            title: {
                type: String,
                required: false,
                default: "TagGroup"
            },
            clear: {
                type: String,
                required: false,
                default: "clear"
            }
        },
        methods: {
            reset() {
                for (let i = 0; i < this.items.length; i++) {
                    this.items[i].selected = false
                }
                let data = [];
                this.$emit('get', data)
            },
            get(index) {
                this.items[index].selected = !this.items[index].selected;
                let data = [];
                for (let i = 0; i < this.items.length; i++) {
                    if (this.items[i].selected) {
                        data.push(this.items[i])
                    }
                }
                this.$emit('get', data)
            }
        }
    }
</script>

<style scoped>
    .tag-group {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        font-family: monospace;
        margin: 2px;
        line-height: 1.5rem;
    }
    .tag-group span {
        float: left;
        height: auto;
        width: auto;
        margin: 5px;
        cursor: pointer;
        color: black;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        background-color: whitesmoke;
        border-radius: 4px;
        display: -ms-inline-flexbox;
        display: inline-flex;
        font-size: 0.75rem;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        justify-content: center;
        line-height: 1.5;
        padding-left: 0.75em;
        padding-right: 0.75em;
        white-space: nowrap;
    }
    .tag-group span:hover {
        background-color: darkgray;
    }
    .tag-group header {
        border-bottom: 1px solid darkgray;
        float: left;
        width: 100%;
    }
    .tag-group header > p {
        float: left;
        text-align: left;
        margin: 1%;
    }
    .tag-group header > button {
        float: left;
        margin: 2%;
        text-align: center;
        outline: none;
        box-shadow: none;
        text-decoration: underline;
        border: none;
        cursor: pointer;
        color: black;
    }
    .tag-group header > button:hover {
        font-weight: bolder;
    }
</style>