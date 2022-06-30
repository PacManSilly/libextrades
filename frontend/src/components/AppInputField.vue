<script setup>
/* eslint-disable */
const props = defineProps({
  modelValue: {type: String},
  label: {type: String, default: "Text"},
  type: {type: String, default: "text"},
  required: {type: Boolean, default: true},
  placeholder: {type: String, default: "Enter value..."},
});

const emit = defineEmits(["update:modelValue"]);
</script>

<template>
  <div class="flex flex-col gap-1">

    <label :for="label" class="text-slate-400 text-xs font-normal md:text-sm">
      {{ props.label }}
    </label>

    <input
      :value="props.modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      :type="type"
      :name="props.label"
      :id="props.label"
      :placeholder="placeholder"
      :required="required"
      class="w-full p-2 bg-slate-100 font-normal text-xs text-slate-900 rounded-sm ring-blue-500 ring-offset-2
      ring-offset-slate-900 transition-all duration-150 hover:ring-2 focus:ring-2 focus:outline-none md:p-2 md:text-sm
      "
    />

  </div>
</template>
