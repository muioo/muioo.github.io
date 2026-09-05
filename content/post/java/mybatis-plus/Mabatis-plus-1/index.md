---
author: muioo

title: "【Mabatis-Plus】MP相关使用"

date: 2026-07-06

description: "Mabatis-plus"

tags: ["MyBatis-Plus"]
categories: ["Java"]
---

## 使用方法

以blog为例mapper需要继承BaseMapper<Blog>

```java
public interface BlogMapper extends BaseMapper<Blog> {
   void incrLiked(@Param("id") Long id, @Param("num") int num);
}
```

ervice中需要继承 IService 这个IService中

```java
public interface IBlogService extends IService<Blog> {

    Result queryBlogById(Long id);
    Result queryHotBlog(Integer current);
    Result likeBlog(Long id);
    Result queryBlogLikes(Long blogId);

    Result saveBlog(Blog blog);

    /**
     * 滚动分页查询当前用户收件箱（关注博主推送的博客）
     * 基于 Redis ZSet 的 score（时间戳）倒序分页，解决传统分页在 Feed 流中数据错位的问题
     *
     * @param lastId 上一次查询返回的最小时间戳，作为本次查询的上界（首次传当前时间+1）
     * @param offset 上一次查询结果中与最小时间戳相等的元素个数，用于跳过重复数据
     * @return 包含 list（博客列表）、minTime（本次最小时间戳）、offset（本次偏移量）的结果
     */
    Result queryBlogOfFollow(Long lastId, Integer offset);
}
```

IService中会继承IRepository接口 这个接口中有默认方法，有增删改查 分页查询等封装好的函数

```java
public interface IService<T> extends IRepository<T> {
    @Transactional(
        rollbackFor = {Exception.class}
    )
    default boolean saveBatch(Collection<T> entityList) {
        return this.saveBatch(entityList, 1000);
    }

    @Transactional(
        rollbackFor = {Exception.class}
    )
    default boolean saveOrUpdateBatch(Collection<T> entityList) {
        return this.saveOrUpdateBatch(entityList, 1000);
    }

    @Transactional(
        rollbackFor = {Exception.class}
    )
    default boolean removeBatchByIds(Collection<?> list) {
        return this.removeByIds(list);
    }

    @Transactional(
        rollbackFor = {Exception.class}
    )
    default boolean updateBatchById(Collection<T> entityList) {
        return this.updateBatchById(entityList, 1000);
    }
}
```

## Mabatis-Plus与Mabatis的区别



## Mabatis-Plus分页查询

方法一：使用pagehelper

```xml
<dependency>
    <groupId>com.github.pagehelper</groupId>
    <artifactId>pagehelper-spring-boot-starter</artifactId>
    <version>1.4.6</version>
</dependency>
```

```java
PageHelper.startPage(current, size);
```

方法二：使用page

```JAVA
public Result<PageResult> getPageEmployee(EmployeePageQueryDTO employeePageQueryDTO) {
// 分页对象
Page<Employee> page = new Page<>(employeePageQueryDTO.getPage(), employeePageQueryDTO.getPageSize());
// 查询条件 wrapper 用于构造条件查询
LambdaQueryWrapper<Employee> wrapper = new LambdaQueryWrapper<>();
wrapper.like(employeePageQueryDTO.getName() != null, Employee::getName, employeePageQueryDTO.getName())
.orderByDesc(Employee::getCreateTime);

// 执行分页
Page<Employee> pageData = this.page(page, wrapper);

PageResult pageResult = new PageResult(pageData.getTotal(), pageData.getRecords());
return Result.success(pageResult);
}
```

## 解决insert和update中字段填充

MetaObjectHandler

```JAVA
@Component
public class MyMetaObjectHandler implements MetaObjectHandler {

    @Override
    public void insertFill(MetaObject metaObject) {
        this.strictInsertFill(metaObject, "createTime", LocalDateTime.class, LocalDateTime.now());
        this.strictInsertFill(metaObject, "updateTime", LocalDateTime.class, LocalDateTime.now());
        this.strictInsertFill(metaObject, "createUser", Long.class, BaseContext.getCurrentId());
        this.strictInsertFill(metaObject, "updateUser", Long.class, BaseContext.getCurrentId());
    }

    @Override
    public void updateFill(MetaObject metaObject) {
        this.strictUpdateFill(metaObject, "updateTime", LocalDateTime.class, LocalDateTime.now());
        this.strictUpdateFill(metaObject, "updateUser", Long.class, BaseContext.getCurrentId());
    }
}
```

employee实体

```JAVA
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@TableName("employee")
public class Employee implements Serializable {

    private static final long serialVersionUID = 1L;

    @TableId(type = IdType.AUTO)
    private Long id;

    private String username;

    private String name;

    private String password;

    private String phone;

    private String sex;

    private String idNumber;

    private Integer status;

    //@JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createTime;

    //@JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;

    @TableField(fill = FieldFill.INSERT)
    private Long createUser;

    @TableField(fill = FieldFill.INSERT_UPDATE)
    private Long updateUser;

}
```

