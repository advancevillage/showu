<template>
    <div class="tooltip" v-bind:style="{width: (label.length * 7) + 'px', marginLeft: '-' + (label.length * 7) >> 1 + 'px'}">
        <span class="context">{{label}}</span>
    </div>
</template>

<script>
    export default {
        name: "ToolTip",
        props: {
            label: {
                type: String,
                required: true
            }
        }
    }
</script>

<style scoped>
    .tooltip {
        position: relative;
        display: inline-block;
    }
    .tooltip .context {
        visibility: hidden;
        position: absolute;
        background-color: #555;
        color: #fff;
        text-align: center;
        padding: 2px 5px;
        border-radius: 6px;
        z-index: 1;
        opacity: 0.8;
        -webkit-transition: opacity .6s;
        transition: opacity .6s;
        bottom: 100%;
        left: 50%;
    }
    .tooltip:hover .context {
        visibility: visible;
    }
</style>