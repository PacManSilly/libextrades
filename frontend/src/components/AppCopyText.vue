<script setup>
/* eslint-disable */
import { reactive, useSlots } from 'vue';
import { copyText } from "vue3-clipboard";

// props
const props = defineProps({
    position: {type: Number, default: 1}
})

// data
const data = reactive({
    copied: false,
})

// slots
const slots = useSlots()

// methods
const copy = () => {
    // get text to copy
    const text = slots.text()[0].children;

    // copy text
    copyText(text, undefined, (error, event) => {})
    
    // use timeout to change text state
    setTimeout(() => {
        data.copied = true
        setTimeout(() => { data.copied = false }, 1500)
    }, 100)
}
</script>

<template>
    <div :class="props.position == 1 ? 'flex-col':'flex-row'" class="w-full inline-flex flex-initial items-center justify-center gap-3">

        <!-- start of button to copy text -->
        <div :class="props.position == 1 ? 'order-1':'order-2'">
            <button @click.prevent="copy" :class="data.copied ? 'bg-blue-400 scale-125':'bg-slate-700'" class="text-xs text-slate-100 p-2 rounded-lg duration-300 shadow-md md:text-sm">
                <slot name="copy" v-if="!data.copied">Copy</slot>
                <slot name="copied" v-else-if="data.copied">Copied!!!</slot>
            </button>
        </div>
        <!-- end of button to copy text -->

        <div :class="props.position == 1 ? 'order-2':'order-1'" class="text-white text-sm font-black md:text-base">
            <slot ref="text" name="text"></slot>
        </div>

    </div>
</template>