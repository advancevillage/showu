<template>
    <button type="button" class="ss_dialog" @click="open">
        <span :class="icon"></span>
    </button>
</template>

<script>
    /**
     * @brief: Dialog 是封装 BueFy 组件，需要加载组件本身关闭打开的对话框。
     * 可参考 Address.vue 实现
     */
    export default {
        name: "Dialog",
        props: {
            params: {
                type: Object,
                required: true
            },
            icon: {
                type: String,
                required: true
            },
        },
        methods: {
            open() {
                let config = {};
                config.props  = this.params.props;
                config.component = this.params.component;
                config.parent = this;
                config.hasModalCard = true;
                config.trapFocus = true;
                config.scroll  = "keep";
                config.events  = {};
                this.$buefy.modal.open(config)
            }
        }
    }
</script>

<style scoped>
    .ss_dialog {

    }
</style>