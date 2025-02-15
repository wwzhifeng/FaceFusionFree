from typing import Any, Dict, Optional

WORDING: Dict[str, Any] = {
    'uis': {
        'start_benchmark': '开始基准测试',
        'benchmark_runs_checkbox_group': '基准测试运行',
        'benchmark_cycles_slider': '基准测试周期',
        # 其他需要汉化的文本可以在这里添加
    },
    'about': {
        'become_a_member': '王知风🍒AI社群',
        'join_our_community': '王知风🍒AI社群',
        'read_the_documentation': '王知风🍒AI社群',
    },
    'error': {
        'file_not_found': '文件未找到',
        'invalid_input': '无效输入',
    },
    # 继续添加其他需要的汉化文本
    'conda_not_activated': 'Conda 未激活',
    'python_not_supported': '不支持的 Python 版本，请升级至 {version} 或更高版本',
    'curl_not_installed': '未安装 CURL',
    'uis.processors_checkbox_group': '处理器选项',
    'ffmpeg_not_installed': '未安装 FFMpeg',
    'creating_temp': '正在创建临时资源',
    'extracting_frames': '正在提取帧，分辨率为 {resolution}，帧率为每秒 {fps} 帧',
    'extracting_frames_succeed': '提取帧成功',
    'extracting_frames_failed': '提取帧失败',
    'analysing': '正在分析',
    'extracting': '正在提取',
    'streaming': '正在流式处理',
    'processing': '正在处理',
    'merging': '正在合并',
    'downloading': '正在下载',
    'temp_frames_not_found': '未找到临时帧',
    'copying_image': '正在复制图像，分辨率为 {resolution}',
    'copying_image_succeed': '复制图像成功',
    'copying_image_failed': '复制图像失败',
    'finalizing_image': '正在完成图像，分辨率为 {resolution}',
    'finalizing_image_succeed': '图像完成',
    'finalizing_image_skipped': '跳过图像完成',
    'merging_video': '正在合并视频，分辨率为 {resolution}，帧率为每秒 {fps} 帧',
    'merging_video_succeed': '合并视频成功',
    'merging_video_failed': '合并视频失败',
    'skipping_audio': '跳过音频',
    'replacing_audio_succeed': '替换音频成功',
    'replacing_audio_skipped': '跳过替换音频',
    'restoring_audio_succeed': '还原音频成功',
    'restoring_audio_skipped': '跳过还原音频',
    'clearing_temp': '正在清理临时资源',
    'processing_stopped': '处理已停止',
    'processing_image_succeed': '图像处理成功，耗时 {seconds} 秒',
    'processing_image_failed': '图像处理失败',
    'processing_video_succeed': '视频处理成功，耗时 {seconds} 秒',
    'processing_video_failed': '视频处理失败',
    'choose_image_source': '请选择用于源的图像',
    'choose_audio_source': '请选择用于源的音频',
    'choose_video_target': '请选择用于目标的视频',
    'choose_image_or_video_target': '请选择用于目标的图像或视频',
    'specify_image_or_video_output': '请在目录中指定输出的图像或视频',
    'match_target_and_output_extension': '目标文件与输出文件的扩展名必须匹配',
    'no_source_face_detected': '未检测到源人脸',
    'processor_not_loaded': '无法加载处理器 {processor}',
    'processor_not_implemented': '处理器 {processor} 未正确实现',
    'ui_layout_not_loaded': '无法加载 UI 布局 {ui_layout}',
    'ui_layout_not_implemented': 'UI 布局 {ui_layout} 未正确实现',
    'stream_not_loaded': '无法加载流模式 {stream_mode}',
    'stream_not_supported': '不支持的流模式',
    'job_created': '已创建任务 {job_id}',
    'job_not_created': '未能创建任务 {job_id}',
    'job_submitted': '已提交任务 {job_id}',
    'job_not_submitted': '未能提交任务 {job_id}',
    'job_all_submitted': '已提交所有任务',
    'job_all_not_submitted': '未能提交所有任务',
    'job_deleted': '已删除任务 {job_id}',
    'job_not_deleted': '未能删除任务 {job_id}',
    'job_all_deleted': '已删除所有任务',
    'job_all_not_deleted': '未能删除所有任务',
    'job_step_added': '已向任务 {job_id} 添加步骤',
    'job_step_not_added': '未能向任务 {job_id} 添加步骤',
    'job_remix_step_added': '已从任务 {job_id} 重混步骤 {step_index}',
    'job_remix_step_not_added': '未能从任务 {job_id} 重混步骤 {step_index}',
    'job_step_inserted': '已向任务 {job_id} 插入步骤 {step_index}',
    'job_step_not_inserted': '未能向任务 {job_id} 插入步骤 {step_index}',
    'job_step_removed': '已从任务 {job_id} 移除步骤 {step_index}',
    'job_step_not_removed': '未能从任务 {job_id} 移除步骤 {step_index}',
    'running_job': '正在运行队列中的任务 {job_id}',
    'running_jobs': '正在运行所有队列中的任务',
    'retrying_job': '正在重试失败的任务 {job_id}',
    'retrying_jobs': '正在重试所有失败的任务',
    'processing_job_succeed': '任务 {job_id} 处理成功',
    'processing_jobs_succeed': '所有任务处理成功',
    'processing_job_failed': '任务 {job_id} 处理失败',
    'processing_jobs_failed': '所有任务处理失败',
    'processing_step': '正在处理第 {step_current} 步，共 {step_total} 步',
    'validating_hash_succeed': '校验 {hash_file_name} 的哈希值成功',
    'validating_hash_failed': '校验 {hash_file_name} 的哈希值失败',
    'validating_source_succeed': '验证 {source_file_name} 的源文件成功',
    'validating_source_failed': '验证 {source_file_name} 的源文件失败',
    'deleting_corrupt_source': '正在删除损坏的源文件 {source_file_name}',
    'time_ago_now': '刚刚',
    'time_ago_minutes': '{minutes} 分钟前',
    'time_ago_hours': '{hours} 小时 {minutes} 分钟前',
    'time_ago_days': '{days} 天 {hours} 小时 {minutes} 分钟前',
    'point': '。',
    'comma': '，',
    'colon': '：',
    'question_mark': '？',
    'exclamation_mark': '！',
    'help': {
        # installer
        'install_dependency': '选择要安装的 {dependency} 变体',
        'skip_conda': '跳过 conda 环境检查',
        # paths
        'config_path': '选择配置文件以覆盖默认设置',
        'temp_path': '指定存放临时资源的目录',
        'jobs_path': '指定存放任务的目录',
        'source_paths': '选择图像或音频路径',
        'target_path': '选择图像或视频路径',
        'output_path': '在目录中指定输出的图像或视频',
        # patterns
        'source_pattern': '选择图像或音频的文件模式',
        'target_pattern': '选择图像或视频的文件模式',
        'output_pattern': '指定图像或视频的输出模式',
        # face detector
        'face_detector_model': '选择用于检测人脸的模型',
        'face_detector_size': '指定提供给人脸检测器的帧尺寸',
        'face_detector_angles': '指定在检测人脸前需要旋转帧的角度',
        'face_detector_score': '根据置信度分数过滤检测到的人脸',
        # face landmarker
        'face_landmarker_model': '选择用于检测人脸关键点的模型',
        'face_landmarker_score': '根据置信度分数过滤检测到的人脸关键点',
        # face selector
        'face_selector_mode': '使用基于参考的跟踪或简单匹配',
        'face_selector_order': '指定检测到的人脸的排序方式',
        'face_selector_age_start': '根据起始年龄过滤检测到的人脸',
        'face_selector_age_end': '根据结束年龄过滤检测到的人脸',
        'face_selector_gender': '根据性别过滤检测到的人脸',
        'face_selector_race': '根据种族过滤检测到的人脸',
        'reference_face_position': '指定用于创建参考人脸的位置',
        'reference_face_distance': '指定参考人脸与目标人脸之间的相似度',
        'reference_frame_number': '指定用于创建参考人脸的帧号',
        # face masker
        'face_occluder_model': '选择用于遮挡人脸的模型',
        'face_parser_model': '选择用于解析面部区域的模型',
        'face_mask_types': '混合使用不同的人脸遮罩类型（可选项：{choices}）',
        'face_mask_blur': '指定应用在方框遮罩上的模糊程度',
        'face_mask_padding': '在方框遮罩的上、右、下、左四个方向上应用填充',
        'face_mask_regions': '选择用于区域遮罩的面部特征（可选项：{choices}）',
        # frame extraction
        'trim_frame_start': '指定目标视频的起始帧',
        'trim_frame_end': '指定目标视频的结束帧',
        'temp_frame_format': '指定临时资源的格式',
        'keep_temp': '处理结束后保留临时资源',
        # output creation
        'output_image_quality': '指定图像质量（对应压缩率）',
        'output_image_resolution': '根据目标图像指定图像输出分辨率',
        'output_audio_encoder': '指定用于音频输出的编码器',
        'output_video_encoder': '指定用于视频输出的编码器',
        'output_video_preset': '在快速视频处理和视频文件大小之间做平衡',
        'output_video_quality': '指定视频质量（对应压缩率）',
        'output_video_resolution': '根据目标视频指定视频输出分辨率',
        'output_video_fps': '根据目标视频指定视频输出帧率',
        'skip_audio': '省略目标视频的音频',
        # processors
        'processors': '加载单个或多个处理器（可选项：{choices}，...）',
        'age_modifier_model': '选择用于改变人脸年龄的模型',
        'age_modifier_direction': '指定年龄变化的方向',
        'deep_swapper_model': '选择用于换脸的模型',
        'deep_swapper_morph': '在源人脸与目标人脸之间进行融合变形',
        'expression_restorer_model': '选择用于还原表情的模型',
        'expression_restorer_factor': '从目标人脸中还原表情的程度',
        'face_debugger_items': '加载单个或多个处理器（可选项：{choices}）',
        'face_editor_model': '选择用于编辑人脸的模型',
        'face_editor_eyebrow_direction': '指定眉毛方向',
        'face_editor_eye_gaze_horizontal': '指定眼睛的水平方向注视',
        'face_editor_eye_gaze_vertical': '指定眼睛的垂直方向注视',
        'face_editor_eye_open_ratio': '指定眼睛睁开的比例',
        'face_editor_lip_open_ratio': '指定嘴唇张开的比例',
        'face_editor_mouth_grim': '指定嘴部撇嘴程度',
        'face_editor_mouth_pout': '指定嘴部噘嘴程度',
        'face_editor_mouth_purse': '指定嘴部抿嘴程度',
        'face_editor_mouth_smile': '指定嘴部微笑程度',
        'face_editor_mouth_position_horizontal': '指定嘴部水平方向位置',
        'face_editor_mouth_position_vertical': '指定嘴部垂直方向位置',
        'face_editor_head_pitch': '指定头部上下俯仰角',
        'face_editor_head_yaw': '指定头部左右偏航角',
        'face_editor_head_roll': '指定头部旋转角',
        'face_enhancer_model': '选择用于增强人脸的模型',
        'face_enhancer_blend': '将增强后的人脸与之前的人脸进行融合',
        'face_enhancer_weight': '指定应用在人脸上的增强程度',
        'face_swapper_model': '选择用于换脸的模型',
        'face_swapper_pixel_boost': '选择换脸时像素提升的分辨率',
        'frame_colorizer_model': '选择用于对帧进行上色的模型',
        'frame_colorizer_size': '指定提供给帧上色器的帧尺寸',
        'frame_colorizer_blend': '将上色后的结果与之前的帧进行融合',
        'frame_enhancer_model': '选择用于增强帧的模型',
        'frame_enhancer_blend': '将增强后的帧与之前的帧进行融合',
        'lip_syncer_model': '选择用于唇形同步的模型',
        # uis
        'open_browser': '当程序就绪后自动打开浏览器',
        'ui_layouts': '启动单个或多个 UI 布局（可选项：{choices}，...）',
        'ui_workflow': '选择 UI 工作流程',
        # execution
        'execution_device_id': '指定用于处理的设备 ID',
        'execution_providers': '使用不同的推理后端（可选项：{choices}，...）',
        'execution_thread_count': '指定处理时的并行线程数',
        'execution_queue_count': '指定每个线程正在处理的帧数量',
        # download
        'download_providers': '使用不同的下载源（可选项：{choices}，...）',
        'download_scope': '指定下载的范围',
        # memory
        'video_memory_strategy': '在快速处理和低显存占用之间进行平衡',
        'system_memory_limit': '限制处理时可用的系统内存',
        # misc
        'log_level': '调整终端中显示的消息严重级别',
        # run
        'run': '运行程序',
        'headless_run': '以无头模式运行程序',
        'batch_run': '以批处理模式运行程序',
        'force_download': '强制自动下载并退出程序',
        # jobs
        'job_id': '指定任务 ID',
        'job_status': '指定任务状态',
        'step_index': '指定步骤索引',
        # job manager
        'job_list': '按照状态列出任务',
        'job_create': '创建一个草稿状态的任务',
        'job_submit': '将一个草稿任务提交为排队任务',
        'job_submit_all': '将所有草稿任务提交为排队任务',
        'job_delete': '删除处于草稿、排队、失败或完成状态的任务',
        'job_delete_all': '删除所有处于草稿、排队、失败和完成状态的任务',
        'job_add_step': '向草稿任务添加一个步骤',
        'job_remix_step': '从一个草稿任务中重混之前的步骤',
        'job_insert_step': '向草稿任务插入一个步骤',
        'job_remove_step': '从草稿任务移除一个步骤',
        # job runner
        'job_run': '运行一个处于排队状态的任务',
        'job_run_all': '运行所有处于排队状态的任务',
        'job_retry': '重试一个失败的任务',
        'job_retry_all': '重试所有失败的任务'
    },
    'about': {
        'become_a_member': '王知风🍒AI社群',
        'join_our_community': '王知风🍒AI社群',
        'read_the_documentation': '王知风🍒AI社群'
    },

    'uis': {
        'age_modifier_direction_slider': '年龄修改器方向',
        'age_modifier_model_dropdown': '年龄修改器模型',
        'apply_button': '应用',
        'benchmark_cycles_slider': '基准测试周期',
        'benchmark_runs_checkbox_group': '基准测试运行',
        'clear_button': '清除',
        'common_options_checkbox_group': '选项',
        'download_providers_checkbox_group': '下载提供者',
        'deep_swapper_model_dropdown': '深度换脸模型',
        'deep_swapper_morph_slider': '深度换脸融合',
        'execution_providers_checkbox_group': '执行提供者',
        'execution_queue_count_slider': '执行队列数量',
        'execution_thread_count_slider': '执行线程数量',
        'expression_restorer_factor_slider': '表情恢复因子',
        'expression_restorer_model_dropdown': '表情恢复模型',
        'face_debugger_items_checkbox_group': '人脸调试项',
        'face_detector_angles_checkbox_group': '人脸检测角度',
        'face_detector_model_dropdown': '人脸检测模型',
        'face_detector_score_slider': '人脸检测评分',
        'face_detector_size_dropdown': '人脸检测尺寸',
        'face_editor_eyebrow_direction_slider': '面部编辑器眉毛方向',
        'face_editor_eye_gaze_horizontal_slider': '面部编辑器眼睛水平注视',
        'face_editor_eye_gaze_vertical_slider': '面部编辑器眼睛垂直注视',
        'face_editor_eye_open_ratio_slider': '面部编辑器眼睛张开比例',
        'face_editor_head_pitch_slider': '面部编辑器头部俯仰',
        'face_editor_head_roll_slider': '面部编辑器头部滚动',
        'face_editor_head_yaw_slider': '面部编辑器头部偏航',
        'face_editor_lip_open_ratio_slider': '面部编辑器嘴唇张开比例',
        'face_editor_model_dropdown': '面部编辑器模型',
        'face_editor_mouth_grim_slider': '面部编辑器嘴部撇嘴',
        'face_editor_mouth_position_horizontal_slider': '面部编辑器嘴部水平位置',
        'face_editor_mouth_position_vertical_slider': '面部编辑器嘴部垂直位置',
        'face_editor_mouth_pout_slider': '面部编辑器嘴部噘嘴',
        'face_editor_mouth_purse_slider': '面部编辑器嘴部抿嘴',
        'face_editor_mouth_smile_slider': '面部编辑器嘴部微笑',
        'face_enhancer_blend_slider': '面部增强混合',
        'face_enhancer_model_dropdown': '面部增强模型',
        'face_enhancer_weight_slider': '面部增强权重',
        'face_landmarker_model_dropdown': '人脸标定模型',
        'face_landmarker_score_slider': '人脸标定评分',
        'face_mask_blur_slider': '面部遮罩模糊',
        'face_mask_padding_bottom_slider': '面部遮罩下边距',
        'face_mask_padding_left_slider': '面部遮罩左边距',
        'face_mask_padding_right_slider': '面部遮罩右边距',
        'face_mask_padding_top_slider': '面部遮罩上边距',
        'face_mask_regions_checkbox_group': '面部遮罩区域',
        'face_mask_types_checkbox_group': '面部遮罩类型',
        'face_selector_age_range_slider': '面部选择器年龄范围',
        'face_selector_gender_dropdown': '面部选择器性别',
        'face_selector_mode_dropdown': '面部选择器模式',
        'face_selector_order_dropdown': '面部选择器顺序',
        'face_selector_race_dropdown': '面部选择器种族',
        'face_swapper_model_dropdown': '换脸模型',
        'face_swapper_pixel_boost_dropdown': '换脸像素提升',
        'face_occluder_model_dropdown': '面部遮挡模型',
        'face_parser_model_dropdown': '面部解析模型',
        'frame_colorizer_blend_slider': '帧上色混合',
        'frame_colorizer_model_dropdown': '帧上色模型',
        'frame_colorizer_size_dropdown': '帧上色尺寸',
        'frame_enhancer_blend_slider': '帧增强混合',
        'frame_enhancer_model_dropdown': '帧增强模型',
        'job_list_status_checkbox_group': '任务状态',
        'job_manager_job_action_dropdown': '任务操作',
        'job_manager_job_id_dropdown': '任务 ID',
        'job_manager_step_index_dropdown': '步骤索引',
        'job_runner_job_action_dropdown': '任务操作',
        'job_runner_job_id_dropdown': '任务 ID',
        'lip_syncer_model_dropdown': '唇形同步模型',
        'log_level_dropdown': '日志级别',
        'output_audio_encoder_dropdown': '音频编码器',
        'output_image_or_video': '输出',
        'output_image_quality_slider': '图像质量',
        'output_image_resolution_dropdown': '图像分辨率',
        'output_path_textbox': '输出路径',
        'output_video_encoder_dropdown': '视频编码器',
        'output_video_fps_slider': '视频帧率',
        'output_video_preset_dropdown': '视频预设',
        'output_video_quality_slider': '视频质量',
        'output_video_resolution_dropdown': '视频分辨率',
        'preview_frame_slider': '预览帧',
        'preview_image': '预览',
        'processors_checkbox_group': '处理器',
        'reference_face_distance_slider': '参考人脸距离',
        'reference_face_gallery': '参考人脸',
        'refresh_button': '刷新',
        'source_file': '源文件',
        'start_button': '开始',
        'stop_button': '停止',
        'system_memory_limit_slider': '系统内存限制',
        'target_file': '目标文件',
        'temp_frame_format_dropdown': '临时帧格式',
        'terminal_textbox': '终端',
        'trim_frame_slider': '修剪帧',
        'ui_workflow': 'UI 工作流',
        'video_memory_strategy_dropdown': '视频内存策略',
        'webcam_fps_slider': '摄像头帧率',
        'webcam_image': '摄像头',
        'webcam_device_id_dropdown': '摄像头设备 ID',
        'webcam_mode_radio': '摄像头模式',
        'webcam_resolution_dropdown': '摄像头分辨率'
    },
}  # 确保字典在此闭合

def get(key: str, default: Optional[str] = None) -> Optional[str]:
    if '.' in key:
        section, name = key.split('.')
        if section in WORDING and name in WORDING.get(section):
            return WORDING.get(section).get(name)
    if key in WORDING:
        return WORDING.get(key)
    return default  # 如果 key 不存在，返回 default
